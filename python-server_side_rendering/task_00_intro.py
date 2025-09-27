import os

def generate_invitations(template, attendees):
    
    if not isinstance(template, str):
        print("The template must be a string")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Attendees must be a list of dictionaries")
        return

   
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    
    for index, attendee in enumerate(attendees, start=1):
        output_text = template
        output_text = output_text.replace("{name}", str(attendee.get("name") or "N/A"))
        output_text = output_text.replace("{event_title}", str(attendee.get("event_title") or "N/A"))
        output_text = output_text.replace("{event_date}", str(attendee.get("event_date") or "N/A"))
        output_text = output_text.replace("{event_location}", str(attendee.get("event_location") or "N/A"))

        filename = f"output_{index}.txt"
        with open(filename, "w") as file:
            file.write(output_text)

        print(f"Created {filename}")
