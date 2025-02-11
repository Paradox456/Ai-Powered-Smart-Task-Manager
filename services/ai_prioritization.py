import numpy as np
from datetime import datetime, timedelta

class AIPrioritization:
    def __init__(self):
        pass

    def calculate_priority(self, tasks):
        """
        Prioritizes tasks based on urgency, importance, and due date.
        """
        prioritized_tasks = []
        for task in tasks:
            urgency_score = self.get_urgency_score(task['due_date'])
            importance_score = self.get_importance_score(task['priority'])
            overall_score = urgency_score + importance_score
            prioritized_tasks.append((task, overall_score))
        
        # Sort tasks by overall score (higher is more important)
        prioritized_tasks.sort(key=lambda x: x[1], reverse=True)
        return [task[0] for task in prioritized_tasks]

    def get_urgency_score(self, due_date):
        """
        Assigns a score based on how soon the task is due.
        """
        try:
            due_date = datetime.strptime(due_date, "%Y-%m-%d")
            days_left = (due_date - datetime.now()).days
            if days_left <= 1:
                return 10  # Very urgent
            elif days_left <= 3:
                return 7
            elif days_left <= 7:
                return 5
            else:
                return 2  # Low urgency
        except ValueError:
            return 0  # Default if date is invalid

    def get_importance_score(self, priority):
        """
        Assigns a score based on task importance (priority level).
        """
        priority_mapping = {"high": 10, "medium": 5, "low": 2}
        return priority_mapping.get(priority.lower(), 0)

# Example Usage
if __name__ == "__main__":
    tasks = [
        {"title": "Finish project", "priority": "high", "due_date": "2025-06-15"},
        {"title": "Buy groceries", "priority": "low", "due_date": "2025-06-10"},
        {"title": "Prepare for meeting", "priority": "medium", "due_date": "2025-06-11"}
    ]
    ai = AIPrioritization()
    prioritized_tasks = ai.calculate_priority(tasks)
    for task in prioritized_tasks:
        print(task)

