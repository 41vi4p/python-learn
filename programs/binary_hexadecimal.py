import tkinter as tk
from tkinter import ttk


class ConversionApp:
   def __init__(self, root):
       self.root = root
       self.root.title("Binary Hexadecimal Conversion App")


       self.create_widgets()


   def create_widgets(self):
       self.input_label = ttk.Label(self.root, text="Input Data:")
       self.input_label.grid(column=0, row=0, padx=10, pady=10)


       self.input_entry = ttk.Entry(self.root, width=50)
       self.input_entry.grid(column=1, row=0, padx=10, pady=10)


       self.input_format = tk.StringVar()
       self.input_format_combobox = ttk.Combobox(self.root, textvariable=self.input_format, state="readonly")
       self.input_format_combobox['values'] = ("Binary", "Decimal", "Hexadecimal", "ASCII")
       self.input_format_combobox.grid(column=2, row=0, padx=10, pady=10)
       self.input_format_combobox.current(0)


       self.convert_button = ttk.Button(self.root, text="Convert", command=self.convert_data)
       self.convert_button.grid(column=1, row=1, padx=10, pady=10)


       self.result_label = ttk.Label(self.root, text="Result:")
       self.result_label.grid(column=0, row=2, padx=10, pady=10)


       self.result_value = tk.StringVar()
       self.result_value_label = ttk.Label(self.root, textvariable=self.result_value)
       self.result_value_label.grid(column=1, row=2, padx=10, pady=10)


       self.output_format = tk.StringVar()
       self.output_format_combobox = ttk.Combobox(self.root, textvariable=self.output_format, state="readonly")
       self.output_format_combobox['values'] = ("Binary", "Decimal", "Hexadecimal", "ASCII")
       self.output_format_combobox.grid(column=2, row=2, padx=10, pady=10)
       self.output_format_combobox.current(1)


   def convert_data(self):
       input_data = self.input_entry.get()
       input_format = self.input_format.get()
       output_format = self.output_format.get()


       try:
           if input_format == "Binary":
               decimal_value = int(input_data, 2)
           elif input_format == "Decimal":
               decimal_value = int(input_data)
           elif input_format == "Hexadecimal":
               decimal_value = int(input_data, 16)
           elif input_format == "ASCII":
               decimal_value = int.from_bytes(input_data.encode(), 'big')


           if output_format == "Binary":
               result = bin(decimal_value)[2:]
           elif output_format == "Decimal":
               result = str(decimal_value)
           elif output_format == "Hexadecimal":
               result = hex(decimal_value)[2:].upper()
           elif output_format == "ASCII":
               result = decimal_value.to_bytes((decimal_value.bit_length() + 7) // 8, 'big').decode()


           self.result_value.set(result)
       except Exception as e:
           self.result_value.set("Error in conversion")


if __name__ == "__main__":
   root = tk.Tk()
   app = ConversionApp(root)
   root.mainloop()
