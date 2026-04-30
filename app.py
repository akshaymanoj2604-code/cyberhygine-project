from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import uuid
from datetime import datetime

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max file size
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recordings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

db = SQLAlchemy(app)

# Database Models
class RecordingSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(36), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    recordings = db.relationship('Recording', backref='session', lazy=True)

class Recording(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('recording_session.id'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    verified = db.Column(db.Boolean, default=False)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect(url_for('admin'))

@app.route('/admin')
def admin():
    sessions = RecordingSession.query.order_by(RecordingSession.created_at.desc()).all()
    return render_template('admin.html', sessions=sessions)

@app.route('/admin/create_session', methods=['POST'])
def create_session():
    token = str(uuid.uuid4())
    session = RecordingSession(token=token)
    db.session.add(session)
    db.session.commit()
    recording_url = url_for('record', token=token, _external=True)
    return jsonify({'success': True, 'recording_url': recording_url, 'token': token})

@app.route('/record/<token>')
def record(token):
    session = RecordingSession.query.filter_by(token=token).first()
    if not session:
        return "Invalid recording link", 404
    return render_template('record.html', token=token)

@app.route('/upload/<token>', methods=['POST'])
def upload_recording(token):
    session = RecordingSession.query.filter_by(token=token).first()
    if not session:
        return jsonify({'error': 'Invalid session'}), 404

    if 'video' not in request.files:
        return jsonify({'error': 'No video file'}), 400

    file = request.files['video']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = secure_filename(f"{token}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.webm")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        recording = Recording(
            session_id=session.id,
            filename=filename,
            original_filename=file.filename
        )
        db.session.add(recording)
        db.session.commit()

        return jsonify({'success': True, 'recording_id': recording.id})

@app.route('/admin/session/<token>')
def admin_session(token):
    session = RecordingSession.query.filter_by(token=token).first()
    if not session:
        return "Session not found", 404
    return render_template('session.html', session=session)

@app.route('/admin/verify/<int:recording_id>', methods=['POST'])
def verify_recording(recording_id):
    recording = Recording.query.get_or_404(recording_id)
    recording.verified = True
    db.session.commit()
    return jsonify({'success': True})

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)