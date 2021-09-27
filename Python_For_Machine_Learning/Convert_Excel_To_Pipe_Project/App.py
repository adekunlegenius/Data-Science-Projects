import tkinter  
from tkinter.constants import *
import os
from tkinter import filedialog
from tkinter import messagebox
from ConvertToPipedelimited import ExcelFile

class CreateApp:


    def app(self):
        self.root = tkinter.Tk()
        self.root.minsize(width=850, height=400)
        
        self.root.title('Convert Excel To Pipe Delimited Text')
        #self.create_side_view()
        self.create_display_view()
        self.create_choose_file()
        self.root.mainloop()
    
    def create_side_view(self):
        side_frame = tkinter.Frame(self.root)
        side_frame.config(width=200, borderwidth=5, border=5, highlightbackground="#FFFFFF" )
        side_frame.grid(row=0, column=0, padx=5, pady=5)
    

    def create_display_view(self):
        
        top_frame = tkinter.Frame(self.root)
        top_frame.config(height=50, width=400)
        top_frame.grid(row=0, column=0, padx=5, pady=5)

        self.display = tkinter.StringVar()
        self.display.set('Select Excel file to convert')
        tkinter.Label(top_frame, textvariable=self.display).grid( row=0)

    def create_choose_file(self):
        center_frame_obj = tkinter.Frame(self.root)
        center_frame_obj.config(width=500)
        center_frame_obj.grid(row=10, column=0, columnspan=2, pady=10, padx=10)

        button = tkinter.Button(center_frame_obj, text='Choose File',  border=2, command=self.choose_file_clicked())
        button.grid(row=10,  column=0, pady=2, padx=2)
        

        self.path_string= tkinter.StringVar()
        self.selected_filename = str('')
        #self.selected_filename.set('')
        self.path_string.set('No file choosen')
        
        
        entry = tkinter.Entry(center_frame_obj, textvariable=self.path_string, state='readonly')
        entry.grid(row=10,  column=1, padx=5, pady=5, sticky=W+E)

        # self.choose_file_validate_message = tkinter.StringVar()
        # choose_file_validate = tkinter.Label(center_frame_obj, textVariable =self.choose_file_validate_message, background='red' )
        # choose_file_validate.grid(row=11, column=1, sticky=W+E)


        # self.subID_validate_message = tkinter.StringVar()
        self.subID_value = tkinter.StringVar()
        #self.subID_value = str('')
        self.subID_value.set('')

        label = tkinter.Label(center_frame_obj, text='Subscriber ID:')
        label.grid(row=15, column=0, pady=5, padx=5)

        entry_sub_id = tkinter.Entry(center_frame_obj, width=110, textvariable=self.subID_value )
        entry_sub_id.grid(row=15, column=1,  padx=5, pady=5)
        
        
        # subID_validate = tkinter.Label(center_frame_obj, textVariable =self.subID_validate_message, background='red' )
        # subID_validate.grid(row=19, column=1, sticky=W+E)

        label_filename = tkinter.Label(center_frame_obj, text='File Selected:')
        label_filename.grid(row=20, column=0, pady=5, padx=5)

        self.filenamebase= tkinter.StringVar()
        self.filenamebase.set('No file selected')

        entry = tkinter.Entry(center_frame_obj, textvariable=self.filenamebase, state='readonly')
        entry.grid(row=20,  column=1, padx=5, pady=5, sticky=W+E)

        self.create_date_view(center_frame_obj)

        button_gen = tkinter.Button(center_frame_obj, text='Generate Text File',  border=2, command=self.generate_text_fileclicked())
        button_gen.grid(row=30,  column=1, pady=2, padx=2, sticky=N+E)

    def create_date_view(self, frame_Obj):

        date_frame = tkinter.Frame(frame_Obj, width=100)
        date_frame.grid(row=25, column=1, pady=5, columnspan=3, sticky=W)

        label_datename = tkinter.Label(frame_Obj, text='Date:')
        label_datename.grid(row=25, column=0, pady=5, padx=5, sticky=W)

        self.year = tkinter.IntVar()
        self.year.set(2021)
        self.prev_year_value = 0

        year_spin_box = tkinter.Spinbox(date_frame, from_=2019, to=2030, width=10, textvariable=self.year )
        year_spin_box.grid(row=25, column=0, padx=5, pady=5)

        self.month = tkinter.IntVar()
        self.month.set(9)
        month_spin_box = tkinter.Spinbox(date_frame, from_=1, to=12, width=10, textvariable=self.month )
        month_spin_box.grid(row=25, column=1, padx=5, pady=5)

        self.day = tkinter.IntVar()
        self.day.set(9)
        day_spin_box = tkinter.Spinbox(date_frame, from_=1, to=31, width=10, textvariable=self.day )
        day_spin_box.grid(row=25, column=2, padx=5, pady=5)
        

    def choose_file_clicked(self):
        global filename
        
        def callback():
            try:
                filename = filedialog.askopenfilename(defaultextension='.xlsx', filetypes=[('All Files', '*.*'), ("Excel Work Book", "*.xlsx"), ("Excel 97-2003 Workbook", "*.xls")])

                if filename == "":
                    filename = None
                    self.selected_filename = filename
                    return
                    
                elif filename.split('.')[-1] not in ['xlsx', 'xls']:
                    messagebox.showinfo("Info", "Only Excel Workbook of type .xlsx and .xls can be selected")
                    return
                else:
                    print(filename)
                    self.selected_filename = filename
                    filenamebase_here = os.path.basename(filename)
                    
                    # path_list = filename.split('/')
                    # path_list.remove(path_list[-1])
                    # print('/'.join(path_list))
                    #print(path_list)

                    #print(self.get_absolute_parent_path(filename))
                    
                    self.filenamebase.set(filenamebase_here)
                    self.path_string.set(filename)
            except:
                messagebox.showerror('Invalid', 'Error loading excel file')
        return callback
        
    def validate(self)->bool:
        
        if self.selected_filename == '':
            print(self.selected_filename)
            print(self.subID_value.get())
            print("Validation Error", "No Excel File choosen yet. Please select a file")
            messagebox.showwarning("Validation Error", "No Excel File choosen yet. Please select a file")              
            return FALSE
        elif self.subID_value.get() == '':
                
            print(self.selected_filename)
            print(self.subID_value.get())
            print("Validation Error", "Subscriber ID value not provided")
            messagebox.showwarning("Validation Error", "Subscriber ID value not provided")
            return FALSE
        else:
            #print(self.selected_filename)
            self.subID_provided = self.subID_value.get().strip()
            print(self.subID_provided)
            print("Validated")
            return TRUE
        

    def generate_text_fileclicked(self):

        def callback():
            if self.validate():
                print(self.selected_filename)
                try:
                    print(self.selected_filename)
                    excel_file_class_Obj = ExcelFile(self.selected_filename, self.subID_provided, '2021-08-12')
                    print('-----------------------------------')
                    #print(type(excel_file_class_Obj.file_path))
                    print(excel_file_class_Obj.file_path)
                    print('Trying to read file')
                    excel_file_class_Obj.read_excel_file()
                    print('read file complete')
                    try:
                        print('-----------------------------------')
                        message = excel_file_class_Obj.write_to_file()
                        print(message)
                    except:
                            messagebox.showerror('Invalid', 'Error writing to text file')                   
               
                except:
                    messagebox.showerror('Invalid', 'Error reading excel file')
                    print(os.error)
            else:
                return
        
        return callback


    
create = CreateApp()
create.app()