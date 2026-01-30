import webbrowser as w

webbrowser={"clever": "https://clever.com/in/miami/student/portal", 
            "iready": "https://login.i-ready.com/student/dashboard/home",
            "ixl": "https://www.ixl.com/dashboard",
            "edusmart": "https://lms.edusmart.com/authenticated/studentDashboard/studentDashboard/0",
            "renaissance": "https://global-zone52.renaissance-go.com/studentportal/",
            "performance matters": "https://olamiami.performancematters.com/ola/ola.jsp?clientCode=flMiamiDade",
            "mcgraw hill": "https://my.mheducation.com",
            "commonlit": "https://www.commonlit.org/students/student_lessons",
            "amira learning": "https://home.app.amiralearning.com/home",
            "discovery education": "https://dadeschools.discoveryeducation.com/learn/explore"} 

ready=True
while ready==True:
        try:
            print("|Clever|")
            print(r"   \_____|Iready|")
            print(r"   \_____|Clever(BASE)|")
            print(r"   \_____|IXL|")
            print(r"   \_____|Edusmart|")
            print(r"   \_____|Renaissance|")
            print(r"   \_____|Performance Matters|")
            print(r"   \_____|McGraw Hill|")
            print(r"   \_____|CommonLit|")
            print(r"   \_____|Amira Learning|")
            print(r"   \_____|Discovery Education|")
            print(r"   \_____|Close?|") 

            converts=input("What program? ").lower()
            if converts=="close":
                ready=False
                break
            else:
                ready=True
            w.open(webbrowser[converts])
        except:
            print("That program is not available.")
