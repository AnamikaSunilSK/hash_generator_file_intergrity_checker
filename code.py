"""
HASH GENERATOR - Live Demo
See how hashes work in real-time
No installations needed!
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import hashlib
import os

class HashGeneratorLive:
    def __init__(self, root):
        self.root = root
        self.root.title("Hash Generator - Digital Fingerprint Tool")
        self.root.geometry("900x750")
        self.root.configure(bg='#1e1e1e')
        
        self.colors = {
            'bg': '#1e1e1e',
            'fg': '#d4d4d4',
            'accent': '#007acc',
            'success': '#4ec9b0',
            'warning': '#dcdcaa',
            'error': '#f48771'
        }
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="🔐 Hash Generator - Digital Fingerprint Tool", 
                        font=("Arial", 16, "bold"),
                        bg=self.colors['bg'], fg=self.colors['accent'])
        title.pack(pady=10)
        
        # Create notebook for tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Tab 1: Text Hash (Interactive)
        self.text_frame = tk.Frame(notebook, bg=self.colors['bg'])
        notebook.add(self.text_frame, text="📝 Text Hash (Live)")
        self.setup_text_tab()
        
        # Tab 2: File Hash
        self.file_frame = tk.Frame(notebook, bg=self.colors['bg'])
        notebook.add(self.file_frame, text="📁 File Hash")
        self.setup_file_tab()
        
        # Tab 3: Password Hash Demo
        self.password_frame = tk.Frame(notebook, bg=self.colors['bg'])
        notebook.add(self.password_frame, text="🔑 Password Hashing Demo")
        self.setup_password_tab()
        
        # Tab 4: Educational
        self.education_frame = tk.Frame(notebook, bg=self.colors['bg'])
        notebook.add(self.education_frame, text="📖 Learn About Hashing")
        self.setup_education_tab()
        
    def setup_text_tab(self):
        """Interactive text hashing with live updates"""
        # Input section
        input_frame = tk.Frame(self.text_frame, bg=self.colors['bg'])
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(input_frame, text="Enter any text:", 
                bg=self.colors['bg'], fg=self.colors['fg'],
                font=("Arial", 10, "bold")).pack(anchor=tk.W)
        
        self.text_input = tk.Text(input_frame, height=5, 
                                  bg='#2d2d2d', fg=self.colors['fg'],
                                  font=("Consolas", 10))
        self.text_input.pack(fill=tk.X, pady=5)
        self.text_input.bind('<KeyRelease>', self.update_hashes_live)
        
        # Example buttons
        example_frame = tk.Frame(self.text_frame, bg=self.colors['bg'])
        example_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Button(example_frame, text="Example: 'password123'", 
                 command=lambda: self.set_example("password123"),
                 bg='#3c3c3c', fg=self.colors['fg']).pack(side=tk.LEFT, padx=2)
        
        tk.Button(example_frame, text="Example: 'password124'", 
                 command=lambda: self.set_example("password124"),
                 bg='#3c3c3c', fg=self.colors['fg']).pack(side=tk.LEFT, padx=2)
        
        tk.Button(example_frame, text="Example: 'Hello World'", 
                 command=lambda: self.set_example("Hello World"),
                 bg='#3c3c3c', fg=self.colors['fg']).pack(side=tk.LEFT, padx=2)
        
        # Hash results frame
        results_frame = tk.LabelFrame(self.text_frame, text="Hash Results (Digital Fingerprints)", 
                                      bg=self.colors['bg'], fg=self.colors['accent'],
                                      font=("Arial", 10, "bold"))
        results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # MD5
        tk.Label(results_frame, text="MD5 (128-bit):", 
                bg=self.colors['bg'], fg=self.colors['warning']).pack(anchor=tk.W, padx=5, pady=(5,0))
        self.md5_result = tk.Text(results_frame, height=1, bg='#2d2d2d', 
                                  fg=self.colors['success'], font=("Consolas", 9))
        self.md5_result.pack(fill=tk.X, padx=5, pady=2)
        
        # SHA1
        tk.Label(results_frame, text="SHA1 (160-bit):", 
                bg=self.colors['bg'], fg=self.colors['warning']).pack(anchor=tk.W, padx=5, pady=(5,0))
        self.sha1_result = tk.Text(results_frame, height=1, bg='#2d2d2d', 
                                   fg=self.colors['success'], font=("Consolas", 9))
        self.sha1_result.pack(fill=tk.X, padx=5, pady=2)
        
        # SHA256
        tk.Label(results_frame, text="SHA256 (256-bit):", 
                bg=self.colors['bg'], fg=self.colors['warning']).pack(anchor=tk.W, padx=5, pady=(5,0))
        self.sha256_result = tk.Text(results_frame, height=1, bg='#2d2d2d', 
                                     fg=self.colors['success'], font=("Consolas", 9))
        self.sha256_result.pack(fill=tk.X, padx=5, pady=2)
        
        # SHA512
        tk.Label(results_frame, text="SHA512 (512-bit):", 
                bg=self.colors['bg'], fg=self.colors['warning']).pack(anchor=tk.W, padx=5, pady=(5,0))
        self.sha512_result = tk.Text(results_frame, height=1, bg='#2d2d2d', 
                                     fg=self.colors['success'], font=("Consolas", 9))
        self.sha512_result.pack(fill=tk.X, padx=5, pady=2)
        
        # Size indicator
        self.size_label = tk.Label(results_frame, text="", 
                                   bg=self.colors['bg'], fg=self.colors['fg'])
        self.size_label.pack(anchor=tk.W, padx=5, pady=5)
        
    def setup_file_tab(self):
        """File hashing with verification"""
        control_frame = tk.Frame(self.file_frame, bg=self.colors['bg'])
        control_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(control_frame, text="📂 Select File", command=self.select_file,
                 bg=self.colors['accent'], fg='white', padx=20).pack(side=tk.LEFT, padx=5)
        
        self.file_label = tk.Label(control_frame, text="No file selected", 
                                   bg=self.colors['bg'], fg=self.colors['fg'])
        self.file_label.pack(side=tk.LEFT, padx=10)
        
        # File info
        self.file_info = tk.Text(self.file_frame, height=3, bg='#2d2d2d', 
                                 fg=self.colors['fg'], font=("Consolas", 9))
        self.file_info.pack(fill=tk.X, padx=10, pady=5)
        
        # Hash results for file
        results_frame = tk.LabelFrame(self.file_frame, text="File Hashes", 
                                      bg=self.colors['bg'], fg=self.colors['accent'])
        results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.file_md5 = tk.Text(results_frame, height=1, bg='#2d2d2d', 
                                fg=self.colors['success'], font=("Consolas", 9))
        self.file_md5.pack(fill=tk.X, padx=5, pady=2)
        
        self.file_sha1 = tk.Text(results_frame, height=1, bg='#2d2d2d', 
                                 fg=self.colors['success'], font=("Consolas", 9))
        self.file_sha1.pack(fill=tk.X, padx=5, pady=2)
        
        self.file_sha256 = tk.Text(results_frame, height=1, bg='#2d2d2d', 
                                   fg=self.colors['success'], font=("Consolas", 9))
        self.file_sha256.pack(fill=tk.X, padx=5, pady=2)
        
        # Integrity check section
        verify_frame = tk.LabelFrame(self.file_frame, text="Verify File Integrity", 
                                     bg=self.colors['bg'], fg=self.colors['accent'])
        verify_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(verify_frame, text="Enter original hash to compare:", 
                bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor=tk.W, padx=5)
        
        self.verify_entry = tk.Entry(verify_frame, bg='#2d2d2d', fg=self.colors['fg'])
        self.verify_entry.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Button(verify_frame, text="Verify Integrity", command=self.verify_integrity,
                 bg=self.colors['accent'], fg='white').pack(pady=5)
        
        self.verify_result = tk.Label(verify_frame, text="", 
                                      bg=self.colors['bg'], font=("Arial", 10, "bold"))
        self.verify_result.pack(pady=5)
        
    def setup_password_tab(self):
        """Password hashing demonstration"""
        demo_frame = tk.Frame(self.password_frame, bg=self.colors['bg'])
        demo_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        tk.Label(demo_frame, text="Why passwords are stored as hashes (not plain text)", 
                bg=self.colors['bg'], fg=self.colors['accent'],
                font=("Arial", 11, "bold")).pack(pady=5)
        
        # Password input
        tk.Label(demo_frame, text="Enter a password:", 
                bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor=tk.W)
        self.password_input = tk.Entry(demo_frame, show="•", width=40,
                                       bg='#2d2d2d', fg=self.colors['fg'])
        self.password_input.pack(fill=tk.X, pady=5)
        self.password_input.bind('<KeyRelease>', self.update_password_hash)
        
        # Show/hide checkbox
        self.show_password = tk.BooleanVar()
        tk.Checkbutton(demo_frame, text="Show password", variable=self.show_password,
                      command=self.toggle_password_show,
                      bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor=tk.W)
        
        # Hash result
        tk.Label(demo_frame, text="Stored in database as (SHA256):", 
                bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor=tk.W, pady=(10,0))
        self.password_hash = tk.Text(demo_frame, height=2, bg='#2d2d2d', 
                                     fg=self.colors['success'], font=("Consolas", 9))
        self.password_hash.pack(fill=tk.X, pady=5)
        
        # Explanation
        explanation = """
        🔐 SECURITY EXPLANATION:
        
        When you create an account on a website:
        1. You enter your password: "MySecret123"
        2. Website hashes it: "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
        3. Website stores ONLY the hash (not your actual password)
        
        When you login later:
        1. You enter "MySecret123"
        2. Website hashes what you typed
        3. Website compares it to stored hash
        4. If they match → correct password!
        
        ✅ Even if hackers steal the database, they only see hashes, not real passwords
        ❌ Hackers can't reverse the hash to get "MySecret123"
        """
        
        explanation_text = tk.Text(demo_frame, height=15, bg='#2d2d2d', 
                                   fg=self.colors['fg'], wrap=tk.WORD)
        explanation_text.pack(fill=tk.BOTH, expand=True, pady=10)
        explanation_text.insert(1.0, explanation)
        explanation_text.config(state=tk.DISABLED)
        
    def setup_education_tab(self):
        """Educational content about hashing"""
        edu_text = scrolledtext.ScrolledText(self.education_frame, 
                                             bg='#2d2d2d', fg=self.colors['fg'],
                                             font=("Arial", 10), wrap=tk.WORD)
        edu_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        content = """
        📚 WHAT IS CRYPTOGRAPHIC HASHING?
        
        A hash function is a mathematical algorithm that converts any data into a fixed-length string of characters.
        
        🔑 KEY PROPERTIES:
        
        1. DETERMINISTIC: Same input = same hash every time
        2. FAST: Can hash any size data quickly
        3. ONE-WAY: Cannot reverse a hash to get original data
        4. AVALANCHE EFFECT: Small change = completely different hash
        5. COLLISION-RESISTANT: Different inputs should never produce same hash
        
        🎯 REAL-WORLD USES:
        
        1. PASSWORD STORAGE
           • Websites never store your actual password
           • They store the hash
           • When you login, they hash your entry and compare
        
        2. FILE INTEGRITY CHECKING
           • Download a file from the internet
           • Website shows hash (e.g., "SHA256: abc123...")
           • You hash your downloaded file
           • If hashes match → file wasn't corrupted or tampered with
        
        3. DIGITAL SIGNATURES
           • Hash the document (creates fingerprint)
           • Encrypt just the small hash (faster than encrypting whole document)
           • Others can verify the signature
        
        4. VIRUS DETECTION
           • Antivirus keeps database of known virus hashes
           • Scans files and compares hashes
           • Match = known virus
        
        5. DATA DEDUPLICATION
           • Cloud storage uses hashes to find duplicate files
           • Store only one copy, reference it multiple times
        
        📊 HASH COMPARISON:
        
        | Algorithm | Output Size | Speed | Security |
        |-----------|-------------|-------|----------|
        | MD5       | 32 chars    | Fast  | Broken (don't use) |
        | SHA1      | 40 chars    | Fast  | Weak (avoid) |
        | SHA256    | 64 chars    | Good  | Strong (recommended) |
        | SHA512    | 128 chars   | Good  | Strongest |
        
        ⚠️ COMMON ATTACKS ON HASHES:
        
        1. RAINBOW TABLES: Precomputed hash lookup tables
           • Defense: Use SALT (random data added before hashing)
        
        2. BRUTE FORCE: Try every possible input
           • Defense: Use strong passwords (high entropy)
        
        3. COLLISION ATTACKS: Find two inputs with same hash
           • Defense: Use SHA256 or SHA512
        
        💡 FUN DEMO TO TRY:
        
        1. Go to the "Text Hash" tab
        2. Type "Hello World"
        3. Change one letter to lowercase ("hello World")
        4. Watch how the hash COMPLETELY changes!
        
        🔬 EXPERIMENT:
        
        Try hashing:
        • A single letter: "A"
        • A word: "Password"
        • A sentence: "The quick brown fox jumps over the lazy dog"
        • An empty string: ""
        
        Notice how every hash is the same length regardless of input size!
        """
        
        edu_text.insert(1.0, content)
        edu_text.config(state=tk.DISABLED)
        
    def set_example(self, text):
        """Set example text"""
        self.text_input.delete(1.0, tk.END)
        self.text_input.insert(1.0, text)
        self.update_hashes_live()
        
    def update_hashes_live(self, event=None):
        """Update hashes in real-time as user types"""
        text = self.text_input.get(1.0, tk.END).rstrip('\n')
        
        # Clear results
        for widget in [self.md5_result, self.sha1_result, self.sha256_result, self.sha512_result]:
            widget.delete(1.0, tk.END)
        
        if not text:
            self.size_label.config(text="No text entered")
            return
        
        # Calculate sizes
        char_count = len(text)
        byte_count = len(text.encode('utf-8'))
        self.size_label.config(text=f"Input size: {char_count} characters, {byte_count} bytes")
        
        # Generate hashes
        data = text.encode('utf-8')
        
        self.md5_result.insert(1.0, hashlib.md5(data).hexdigest())
        self.sha1_result.insert(1.0, hashlib.sha1(data).hexdigest())
        self.sha256_result.insert(1.0, hashlib.sha256(data).hexdigest())
        self.sha512_result.insert(1.0, hashlib.sha512(data).hexdigest())
        
    def update_password_hash(self, event=None):
        """Update password hash demo"""
        password = self.password_input.get()
        if password:
            hash_value = hashlib.sha256(password.encode()).hexdigest()
            self.password_hash.delete(1.0, tk.END)
            self.password_hash.insert(1.0, hash_value)
        else:
            self.password_hash.delete(1.0, tk.END)
    
    def toggle_password_show(self):
        """Toggle password visibility"""
        if self.show_password.get():
            self.password_input.config(show="")
        else:
            self.password_input.config(show="•")
    
    def select_file(self):
        """Select file for hashing"""
        from tkinter import filedialog
        filename = filedialog.askopenfilename()
        if filename:
            self.current_file = filename
            self.file_label.config(text=os.path.basename(filename))
            
            # Show file info
            file_size = os.path.getsize(filename)
            self.file_info.delete(1.0, tk.END)
            self.file_info.insert(1.0, f"File: {filename}\nSize: {file_size:,} bytes ({file_size/1024:.2f} KB)")
            
            # Calculate hashes
            with open(filename, 'rb') as f:
                data = f.read()
                
                self.file_md5.delete(1.0, tk.END)
                self.file_md5.insert(1.0, f"MD5: {hashlib.md5(data).hexdigest()}")
                
                self.file_sha1.delete(1.0, tk.END)
                self.file_sha1.insert(1.0, f"SHA1: {hashlib.sha1(data).hexdigest()}")
                
                self.file_sha256.delete(1.0, tk.END)
                self.file_sha256.insert(1.0, f"SHA256: {hashlib.sha256(data).hexdigest()}")
    
    def verify_integrity(self):
        """Verify file integrity against provided hash"""
        if not hasattr(self, 'current_file'):
            messagebox.showwarning("No File", "Please select a file first")
            return
        
        original_hash = self.verify_entry.get().strip()
        if not original_hash:
            messagebox.showwarning("No Hash", "Please enter the original hash to compare")
            return
        
        # Determine hash type by length
        if len(original_hash) == 32:
            hash_type = "md5"
        elif len(original_hash) == 40:
            hash_type = "sha1"
        elif len(original_hash) == 64:
            hash_type = "sha256"
        else:
            self.verify_result.config(text="❌ Unknown hash format (use MD5, SHA1, or SHA256)", 
                                     fg=self.colors['error'])
            return
        
        # Calculate current hash
        with open(self.current_file, 'rb') as f:
            data = f.read()
            if hash_type == "md5":
                current_hash = hashlib.md5(data).hexdigest()
            elif hash_type == "sha1":
                current_hash = hashlib.sha1(data).hexdigest()
            else:
                current_hash = hashlib.sha256(data).hexdigest()
        
        if current_hash == original_hash:
            self.verify_result.config(text="✅ VERIFIED: File integrity confirmed! File has NOT been modified.", 
                                     fg=self.colors['success'])
        else:
            self.verify_result.config(text="❌ FAILED: File has been MODIFIED or CORRUPTED!", 
                                     fg=self.colors['error'])

if __name__ == "__main__":
    root = tk.Tk()
    app = HashGeneratorLive(root)
    root.mainloop()