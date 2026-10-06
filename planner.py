def create_plan(subject, days, study_hours):

    plan = {}

    topics = {
        "Python": [
            "Python Basics",
            "Variables and Data Types",
            "Conditional Statements",
            "Loops",
            "Functions",
            "Lists and Tuples",
            "Dictionaries and Sets",
            "Object-Oriented Programming",
            "File Handling",
            "Exception Handling",
            "Modules and Packages",
            "Practice Problems"
        ],

        "Java": [
            "Java Basics",
            "Variables and Data Types",
            "Operators",
            "Conditional Statements",
            "Loops",
            "Arrays",
            "Methods",
            "Classes and Objects",
            "Inheritance",
            "Polymorphism",
            "Exception Handling",
            "Practice Problems"
        ],

        "Data Structures": [
            "Introduction to Data Structures",
            "Arrays",
            "Linked Lists",
            "Stacks",
            "Queues",
            "Hash Tables",
            "Trees",
            "Binary Search Trees",
            "Graphs",
            "Sorting Algorithms",
            "Searching Algorithms",
            "Practice Problems"
        ],

        "Machine Learning": [
            "Introduction to Machine Learning",
            "Python for Machine Learning",
            "NumPy",
            "Pandas",
            "Data Cleaning",
            "Data Visualization",
            "Linear Regression",
            "Logistic Regression",
            "Decision Trees",
            "Random Forest",
            "Model Evaluation",
            "Practice Project"
        ]
    }

    selected_topics = topics.get(
        subject,
        ["Introduction", "Basics", "Intermediate Concepts", "Advanced Concepts"]
    )

    for day in range(1, days + 1):

        topic = selected_topics[(day - 1) % len(selected_topics)]

        plan[f"Day {day}"] = {
            "topic": topic,
            "hours": study_hours
        }

    return plan


def create_daily_schedule(subject, study_hours):

    schedule = [
        {
            "time": "09:00 AM",
            "activity": f"Study {subject}",
            "duration": f"{study_hours / 2:.1f} hours"
        },

        {
            "time": "11:00 AM",
            "activity": "Practice Questions",
            "duration": "1 hour"
        },

        {
            "time": "02:00 PM",
            "activity": "Revision",
            "duration": "30 minutes"
        },

        {
            "time": "05:00 PM",
            "activity": "Practice / Mini Project",
            "duration": f"{study_hours / 2:.1f} hours"
        }
    ]

    return schedule