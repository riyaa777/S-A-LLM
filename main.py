import openai_utils
import app_controller
from document_controller import search_and_chat_with_documents
import document_controller

print("Welcome to the GCraft!")

on_mode = "GcraftGPT"  # Default to ChatGPT mode

while True:
    user_input = input(f"[Mode: {on_mode}] > ").strip().lower()

    if user_input == "exit":
        print("Goodbye!")
        break
    elif user_input == "1":
        on_mode = "GcraftGPT"
        print("Switched to GcraftGPT mode.")
    elif user_input == "2":
        on_mode = "Local Documents"
        print("Switched to Local Documents mode.")
    elif user_input.startswith("open "):
        app_to_open = user_input[len("open "):]
        if app_to_open in app_controller.get_app_names():
            app_controller.open_app(app_to_open)
            print(f"Opening {app_to_open} app.")
        else:
            print(f"{app_to_open} app not found.")
    else:
        if on_mode == "Local Documents":
            if user_input.startswith("search documents for:"):
                search_query = user_input[len("search documents for:"):]
                search_results = search_and_chat_with_documents(search_query, "documents_folder")
                for result in search_results:
                    print(result)
            else:
                print("Invalid query format for Local Documents mode.")
        else:
            response = openai_utils.generate_response(user_input)
            print(response)
