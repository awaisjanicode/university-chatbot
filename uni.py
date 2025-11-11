# university_chatbot_large.py

# Expanded knowledge base
faq_data = {
    "admission process": "You can apply online through the university admission portal. The last date is 15th September.",
    "admission requirements": "You need your high school transcripts, CNIC, and passport-sized photos for admission.",
    "faculty list": "Visit the Faculty section on our website to view details of all teaching staff.",
    "faculty contact": "You can contact faculty members via email listed on the university website.",
    "course details": "Our university offers BS, MS, and PhD programs in Computer Science, Mathematics, and Management.",
    "course duration": "BS programs are 4 years, MS are 2 years, and PhD durations vary by research.",
    "exam schedule": "The final exam schedule will be announced on the notice board and the student portal.",
    "exam rules": "No electronic devices are allowed in the exam hall. Late arrivals may not be permitted.",
    "library timing": "The library is open from 8 AM to 8 PM, Monday to Friday.",
    "library rules": "Maintain silence, no food or drinks, return books on time to avoid fines.",
    "hostel timing": "Hostels are open 24/7 but students must follow curfew rules on weekends.",
    "hostel fees": "Monthly hostel fees are $150, payable at the start of each month.",
    "scholarships": "Merit-based and need-based scholarships are available. Apply through the financial aid office.",
    "transportation": "University buses operate from 7 AM to 10 PM covering main city areas.",
    "cafeteria timing": "Cafeteria is open from 8 AM to 8 PM, offering meals and snacks.",
    "student portal": "You can access the student portal with your university ID to view results, attendance, and notices.",
    "result announcement": "Results are published online and on the notice board after grading is complete.",
    "chairman contact": "You can contact the department chairman at chairman@university.edu.",
    "IT support": "For IT help, contact it_support@university.edu or visit the IT department office.",
    "sports facilities": "The university has a gym, football field, cricket ground, and indoor courts.",
    "clubs and societies": "We have debate, coding, drama, and cultural clubs. Join via the student affairs office.",
    "graduation requirements": "Complete all required courses, meet CGPA minimum, and submit clearance forms.",
    "fee payment": "Fees can be paid online through the university portal or at the finance office.",
    "transport pass": "Students can apply for a transport pass at the campus transport office.",
    "holiday schedule": "University holidays are announced at the start of each semester on the website."
}

def chatbot():
    print("🎓 University Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day 🎓")
            break

        # Search for matching questions
        response_found = False
        for key in faq_data:
            if key in user_input:
                print(f"Chatbot: {faq_data[key]}")
                response_found = True
                break
        
        if not response_found:
            print("Chatbot: Sorry, I don't have an answer for that. Please contact admin@university.edu.")

if __name__ == "__main__":
    chatbot()
