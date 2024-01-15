
def init_tasks():
    return [
        {'id': 1, 'description': "Complete Project Proposal", 'assigned_to': "John Doe", "subtasks": [
            {'id': 2, 'description': "Research", 'assigned_to': "Alice Brown", 'time_estimate': 5},
            {'id': 3, 'description': "Outline", 'assigned_to': "Bob Johnson",'time_estimate': 3, 'subtasks': [
                {'id': 4, 'description': "Introduction", 'assigned_to': "Jane Smith", 'time_estimate': 3},
                {'id': 5, 'description': "Body", 'assigned_to': "Jane Smith", 'time_estimate': 6},
                {'id': 6, 'description': "Conclusion", 'assigned_to': "David Wilson", 'time_estimate': 2}
                ]}
        ]}]

def main():
    tasks = init_tasks()


if __name__ == "__main__":
    main()