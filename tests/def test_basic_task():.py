def test_metadata_from_tasks():
    task_text = Task.from_text("""---
    name: Take out the trash
    due_date: 5 Aug 2022
    ---

    The trash runs on Thursday
    """)

    assert task.name == "Take out the trash"
    assert task.due_date == datetime(2022, 8, 5)
    assert task.description == "The trash runs on Thursday"
    