#Instrument Power Plant Machine Equipment

def get_response(message):
    message = message.lower()
    if "plc" in message:
        return "PLC (Programmable Logic Controller) is functioning properly."
    elif "transmitter" in message:
        return "Transmitter is calibrated and working within expected ranges."
    elif "chemical" in message:
        return "Chemical processing unit is operating at optimal levels."
    elif "scada" in message:
        return "SCADA (Supervisory Control and Data Acquisition) system is online and monitoring all processes."
    elif "sensor" in message:
        return "All sensors are active and transmitting data correctly."
    elif "Maintenance" in message:
        return "Next scheduled maintenance is in 30 days."
    elif "error" in message or "issue" in message:
        return "Please provide the error code for further assistance."
    else:
        return "I'm not sure how to respond to that. Can you ask something specific about PLC, Transmitter, Chemical, SCADA or Sensor?"


import tkinter as tk
from tkinter import scrolledtext

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Instrument Machinery Chatbot")

        self.title_label = tk.Label(root, text="Machinery Equipment Chatbot", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry_var = tk.StringVar()
        self.entry_box = tk.Entry(root, textvariable=self.entry_var)
        self.entry_box.bind("<Return>", self.send_message)
        self.entry_box.pack(padx=10, pady=10, fill=tk.X)
        
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=10)
        
    def send_message(self, event=None):
        user_message = self.entry_var.get().strip()
        if user_message:
            self.update_chat_area("You: " + user_message)
            self.entry_var.set("")
            response = get_response(user_message)
            self.update_chat_area("Bot: " + response)
        
    def update_chat_area(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.geometry("400x500")
    root.mainloop()
