import tkinter as tk
from tkinter import font as tkfont


class MatchMyCareerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MatchMyCareer")
        self.root.geometry("400x700")
        self.root.configure(bg="#0b1220")

        # Custom Fonts
        self.card_title_font = tkfont.Font(family="Helvetica", size=14, weight="bold")
        self.company_font = tkfont.Font(family="Helvetica", size=10, weight="bold")
        self.normal_font = tkfont.Font(family="Helvetica", size=10)
        self.small_font = tkfont.Font(family="Helvetica", size=9)

        # Job Data Mapping
        self.job_database = {
            "BSIT": [
                {"company": "Google", "role": "Software Developer", "type": "Remote"},
                {"company": "Google", "role": "Cloud Architect", "type": "Hybrid"},
                {"company": "Accenture", "role": "Data Analyst", "type": "Hybrid"},
                {"company": "Accenture", "role": "Systems Admin", "type": "On-site"},
                {"company": "Meta", "role": "Web Developer", "type": "On-site"}
            ],
            "BSTM": [
                {"company": "Expedia", "role": "Travel Consultant", "type": "Remote"},
                {"company": "PAL", "role": "Flight Attendant", "type": "On-site"},
                {"company": "Agoda", "role": "Tourism Officer", "type": "Hybrid"}
            ],
            "BSHM": [
                {"company": "Marriott", "role": "Hotel Manager", "type": "On-site"},
                {"company": "Hilton", "role": "Front Desk Officer", "type": "On-site"},
                {"company": "Viking", "role": "Chef de Partie", "type": "On-site"}
            ],
            "HRDM": [
                {"company": "McDonald's", "role": "HR Generalist", "type": "On-site"},
                {"company": "McDonald's", "role": "Recruitment Specialist", "type": "Hybrid"},
                {"company": "IBM", "role": "HR Specialist", "type": "Hybrid"},
                {"company": "LinkedIn", "role": "Recruiter", "type": "Remote"},
                {"company": "Oracle", "role": "Training Coordinator", "type": "On-site"}
            ]
        }

        self.setup_home_ui()

    def clear_window(self):
        """Removes all widgets from the current window"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def setup_home_ui(self):
        self.clear_window()

        # --- Header ---
        header = tk.Frame(self.root, bg="#0f1b33", height=60)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)
        tk.Label(header, text="MatchMyCareer", fg="#38bdf8", bg="#0f1b33",
                 font=("Helvetica", 14, "bold")).pack(side="left", padx=20)

        # --- Hero Card ---
        hero_card = tk.Frame(self.root, bg="#111c36", padx=20, pady=20)
        hero_card.pack(fill="x", padx=20, pady=20)

        tk.Label(hero_card, text="Ready to Level Up?", fg="#ffffff", bg="#111c36",
                 font=self.card_title_font).pack(anchor="w")

        tk.Label(hero_card, text="Choose how you want to proceed:",
                 fg="#cbd5e1", bg="#111c36", font=self.normal_font).pack(anchor="w", pady=(5, 15))

        btn_insert = tk.Button(hero_card, text="Insert File", bg="#38bdf8", fg="#0b1220",
                               font=("Helvetica", 10, "bold"), bd=0, padx=15, pady=8,
                               width=15, cursor="hand2", command=self.show_upload_slide)
        btn_insert.pack(anchor="w", pady=5)

        btn_make = tk.Button(hero_card, text="Make a Resume", bg="#1e293b", fg="white",
                             font=("Helvetica", 10, "bold"), bd=1, relief="flat", padx=15, pady=8,
                             width=15, cursor="hand2", command=self.show_resume_form_slide)
        btn_make.pack(anchor="w", pady=5)

        tk.Label(self.root, text="RECENT MATCHES", fg="#94a3b8", bg="#0b1220",
                 font=("Helvetica", 8, "bold")).pack(anchor="w", padx=25, pady=(10, 5))
        self.create_mini_job_card("Google", "Software Developer")
        self.create_mini_job_card("Accenture", "Data Analyst")

    def create_mini_job_card(self, company, role):
        card = tk.Frame(self.root, bg="#111c36", padx=15, pady=12)
        card.pack(fill="x", padx=20, pady=5)
        tk.Label(card, text=company, fg="#38bdf8", bg="#111c36", font=("Helvetica", 8, "bold")).pack(anchor="w")
        tk.Label(card, text=role, fg="#ffffff", bg="#111c36", font=("Helvetica", 10)).pack(anchor="w")

    def show_upload_slide(self):
        self.clear_window()
        tk.Label(self.root, text="Upload Center", fg="#38bdf8", bg="#0b1220",
                 font=self.card_title_font).pack(pady=40)

        box = tk.Frame(self.root, bg="#111c36", padx=20, pady=40, highlightbackground="#38bdf8", highlightthickness=1)
        box.pack(padx=40, fill="x")

        tk.Label(box, text="Select PDF or Docx file", fg="white", bg="#111c36").pack()

        # Submit Button for Upload
        tk.Button(self.root, text="Submit File", bg="#38bdf8", fg="#0b1220",
                  font=("Helvetica", 10, "bold"), bd=0, padx=20, pady=10, cursor="hand2",
                  command=self.process_file_upload).pack(pady=20)

        tk.Button(self.root, text="← Back", fg="#94a3b8", bg="#0b1220", bd=0,
                  command=self.setup_home_ui).pack()

    def process_file_upload(self):
        # Loading State
        self.clear_window()
        tk.Label(self.root, text="Analyzing Resume...", fg="#38bdf8", bg="#0b1220",
                 font=self.normal_font).pack(expand=True)

        # After 2 seconds, redirect to HRDM Companies
        self.root.after(2000, lambda: self.handle_submit_direct("HRDM"))

    def show_resume_form_slide(self):
        self.clear_window()
        tk.Label(self.root, text="Resume Builder", fg="#38bdf8", bg="#0b1220",
                 font=self.card_title_font).pack(pady=20)

        form_container = tk.Frame(self.root, bg="#0b1220", padx=40)
        form_container.pack(fill="both")

        for field in ["First Name", "Surname", "Email Address", "Skills"]:
            tk.Label(form_container, text=field, fg="#cbd5e1", bg="#0b1220", font=self.small_font).pack(anchor="w",
                                                                                                        pady=(8, 2))
            tk.Entry(form_container, bg="#111c36", fg="white", insertbackground="white", bd=0).pack(fill="x", ipady=8)

        tk.Label(form_container, text="Course", fg="#cbd5e1", bg="#0b1220", font=self.small_font).pack(anchor="w",
                                                                                                       pady=(8, 2))
        self.course_var = tk.StringVar(self.root)
        self.course_var.set("BSIT")
        course_menu = tk.OptionMenu(form_container, self.course_var, "BSIT", "BSTM", "BSHM", "HRDM")
        course_menu.config(bg="#111c36", fg="white", bd=0, highlightthickness=0, activebackground="#1e293b",
                           font=self.normal_font)
        course_menu["menu"].config(bg="#111c36", fg="white", font=self.normal_font)
        course_menu.pack(fill="x", ipady=5)

        tk.Button(self.root, text="Submit", bg="#38bdf8", fg="#0b1220",
                  font=("Helvetica", 10, "bold"), bd=0, pady=10, cursor="hand2",
                  command=self.handle_submit).pack(pady=30)

        tk.Button(self.root, text="← Back", fg="#94a3b8", bg="#0b1220", bd=0,
                  command=self.setup_home_ui).pack()

    def handle_submit(self):
        selected_course = self.course_var.get()
        self.handle_submit_direct(selected_course)

    def handle_submit_direct(self, course_name):
        # Shared logic to list companies for a specific course
        all_jobs = self.job_database.get(course_name, [])
        companies = sorted(list(set(job["company"] for job in all_jobs)))
        self.show_company_list(course_name, companies)

    def show_company_list(self, course_name, companies):
        self.clear_window()
        tk.Label(self.root, text="Available Companies", fg="#38bdf8", bg="#0b1220", font=self.card_title_font).pack(
            pady=20)
        tk.Label(self.root, text=f"Matches for {course_name}", fg="#cbd5e1", bg="#0b1220", font=self.small_font).pack()

        for company in companies:
            card = tk.Frame(self.root, bg="#111c36", padx=20, pady=15)
            card.pack(fill="x", padx=30, pady=10)

            tk.Label(card, text=company, fg="#ffffff", bg="#111c36", font=("Helvetica", 11, "bold")).pack(side="left")

            tk.Button(card, text="View Work", bg="#38bdf8", fg="#0b1220", font=("Helvetica", 9, "bold"), bd=0, padx=10,
                      pady=5, command=lambda c=company: self.filter_jobs_by_company(course_name, c)).pack(side="right")

        tk.Button(self.root, text="← Back", fg="#94a3b8", bg="#0b1220", bd=0, command=self.setup_home_ui).pack(pady=20)

    def filter_jobs_by_company(self, course_name, company_name):
        all_jobs = self.job_database.get(course_name, [])
        company_jobs = [j for j in all_jobs if j["company"] == company_name]
        self.show_jobs_slide(course_name, company_jobs)

    def show_jobs_slide(self, course_name, jobs):
        self.clear_window()
        company_name = jobs[0]["company"] if jobs else "Company"
        tk.Label(self.root, text=f"Work at {company_name}", fg="#38bdf8", bg="#0b1220", font=self.card_title_font).pack(
            pady=20)

        for job in jobs:
            card = tk.Frame(self.root, bg="#111c36", padx=20, pady=15)
            card.pack(fill="x", padx=20, pady=10)

            info_frame = tk.Frame(card, bg="#111c36")
            info_frame.pack(side="left", fill="x", expand=True)

            tk.Label(info_frame, text=job["company"].upper(), fg="#38bdf8", bg="#111c36",
                     font=("Helvetica", 9, "bold")).pack(anchor="w")
            tk.Label(info_frame, text=job["role"], fg="#ffffff", bg="#111c36", font=("Helvetica", 12, "bold")).pack(
                anchor="w")
            tk.Label(info_frame, text=f"Type: {job['type']}", fg="#94a3b8", bg="#111c36", font=self.small_font).pack(
                anchor="w")

            tk.Button(card, text="Apply", bg="#38bdf8", fg="#0b1220", font=("Helvetica", 9, "bold"), bd=0, padx=10,
                      pady=5,
                      command=lambda j=job: self.show_terms_slide(j)).pack(side="right")

        # Returns to company selection
        tk.Button(self.root, text="← Back to Companies", fg="#94a3b8", bg="#0b1220", bd=0,
                  command=lambda: self.handle_submit_direct(course_name)).pack(pady=20)

    def show_terms_slide(self, job):
        self.clear_window()
        tk.Label(self.root, text="Terms and Conditions for Employees\n"
                                 "Application System Usage Agreement", fg="#38bdf8", bg="#0b1220",
                 font=self.card_title_font).pack(
            pady=15)

        terms_frame = tk.Frame(self.root, bg="#111c36")
        terms_frame.pack(padx=30, fill="both", expand=True)

        scrollbar = tk.Scrollbar(terms_frame)
        scrollbar.pack(side="right", fill="y")

        terms_display = tk.Text(terms_frame, bg="#111c36", fg="#cbd5e1", font=self.small_font,
                                wrap="word", bd=0, yscrollcommand=scrollbar.set, padx=10, pady=10)
        terms_display.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=terms_display.yview)

        full_terms = (f"Application for: {job['role']} at {job['company']}\n\n"
                      "Terms and Conditions for Employees\n"
                      "Application System Usage Agreement\n\n"
                      "1. Responsibility for Communication\n"
                      "Employees are responsible for regularly checking their email, system notifications, and messages.\n\n"
                      "2. Account Security\n"
                      "Keep login credentials confidential. Any activity performed using your account is your responsibility.\n\n"
                      "3. Accurate Information\n"
                      "You are required to provide accurate and updated personal and work-related information.\n\n"
                      "4. Proper Use of the System\n"
                      "The system must only be used for authorized company-related purposes.\n\n"
                      "5. Compliance with Company Policies\n"
                      "Violation of company rules may result in disciplinary action.\n\n"
                      "6. Data Privacy and Confidentiality\n"
                      "Unauthorized sharing or disclosure of information is strictly prohibited.\n\n"
                      "7. Acceptance of Terms\n"
                      "By using the system, you acknowledge you have read and agreed to these terms."
                      )

        terms_display.insert("1.0", full_terms)
        terms_display.config(state="disabled")

        self.agree_var = tk.IntVar()
        tk.Checkbutton(self.root, text="I have read and agree to the terms", variable=self.agree_var,
                       bg="#0b1220", fg="#38bdf8", selectcolor="#111c36", activebackground="#0b1220",
                       font=self.small_font).pack(pady=10)

        tk.Button(self.root, text="Confirm Application", bg="#38bdf8", fg="#0b1220", font=("Helvetica", 10, "bold"),
                  bd=0, padx=20, pady=10, command=self.process_application).pack(pady=(0, 20))

    def process_application(self):
        if self.agree_var.get() == 1:
            self.clear_window()
            tk.Label(self.root, text="Processing Application...", fg="#38bdf8", bg="#0b1220",
                     font=self.normal_font).pack(expand=True)
            self.root.after(2000, self.show_thank_you_slide)

    def show_thank_you_slide(self):
        self.clear_window()
        tk.Label(self.root, text="Success!", fg="#38bdf8", bg="#0b1220", font=("Helvetica", 24, "bold")).pack(
            pady=(150, 10))
        tk.Label(self.root, text="Thank you for applying!", fg="#ffffff", bg="#0b1220", font=self.normal_font).pack()
        tk.Label(self.root, text="Please wait for the results.\nRecruiters will contact you via email.",
                 fg="#cbd5e1", bg="#0b1220", font=self.small_font, justify="center").pack(pady=20)

        tk.Button(self.root, text="Done", bg="#38bdf8", fg="#0b1220", font=("Helvetica", 10, "bold"),
                  bd=0, padx=30, pady=10, command=self.setup_home_ui).pack(pady=40)


if __name__ == "__main__":
    root = tk.Tk()
    app = MatchMyCareerApp(root)
    root.mainloop()