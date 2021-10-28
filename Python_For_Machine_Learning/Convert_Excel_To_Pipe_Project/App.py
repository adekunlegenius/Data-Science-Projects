import tkinter  
from tkinter.constants import *
import os
from tkinter import Canvas, Frame, filedialog
from tkinter import messagebox
from tkinter import ttk
from ConvertToPipedelimited import ExcelFile
from DateFormated import DateFormated
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
        top_frame.config(height=50)
        top_frame.grid(row=0, column=1, padx=5, pady=5, sticky=W+E)

        
        self.display = tkinter.StringVar()
        self.display.set('Select Excel file to convert')
        tkinter.Label(top_frame, textvariable=self.display).grid( row=0, ipady=5)

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

        entry_sub_id = tkinter.Entry(center_frame_obj, textvariable=self.subID_value )
        entry_sub_id.grid(row=15, column=1,  padx=5, pady=5, sticky=W+E)
        
        
        # subID_validate = tkinter.Label(center_frame_obj, textVariable =self.subID_validate_message, background='red' )
        # subID_validate.grid(row=19, column=1, sticky=W+E)

        label_filename = tkinter.Label(center_frame_obj, text='File Selected:')
        label_filename.grid(row=20, column=0, pady=5, padx=5)

        self.filenamebase= tkinter.StringVar()
        self.filenamebase.set('No file selected')

        entry = tkinter.Entry(center_frame_obj, textvariable=self.filenamebase, state='readonly')
        entry.grid(row=20,  column=1, padx=5, pady=5, sticky=W+E)

        self.create_date_view(center_frame_obj)
        self.create_acct_status_checkbox(center_frame_obj)

        button_gen = tkinter.Button(center_frame_obj, text='Generate Text File',  border=2, command=self.generate_text_fileclicked())
        button_gen.grid(row=30,  column=1, pady=2, padx=2, sticky=N+E)

        self.create_display_canvas(center_frame_obj)


    def create_date_view(self, frame_Obj):

        global day_month_feb, day_month_thirty, day_month_thirty_first, month_values, year_values; 
        day_month_feb=list(range(1, 29))
        day_month_thirty = list(range(1, 31))
        day_month_thirty_first = list(range(1, 32))
        month_values = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        date_frame = tkinter.Frame(frame_Obj, width=100)
        date_frame.grid(row=25, column=1, pady=5, columnspan=3, sticky=W)

        label_datename = tkinter.Label(frame_Obj, text='Date:')
        label_datename.grid(row=25, column=0, pady=5, padx=5, sticky=W)

        date_formated_Obj = DateFormated('2021-10-09')
        today_year = date_formated_Obj.get_today_year()
        today_month = date_formated_Obj.get_today_month()

        year_values = list(range((today_year-2), (today_year+10)))
        
        #self.month_values = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        #day_month_thirty_first = day_month_feb.append(['29', '30', '31'])

        
        self.year = tkinter.IntVar()
        self.year.set(today_year)
        self.prev_year_value = 0

        #year_spin_box = tkinter.Spinbox(date_frame, from_=2019, to=2030, width=10, textvariable=self.year )
        year_combo_box = ttk.Combobox(date_frame, textvariable=self.year, width=10)
        year_combo_box['values'] = year_values
        year_combo_box.grid(row=25, column=0, padx=5, pady=5)


        self.month = tkinter.StringVar() #Initialize the string variable
        self.month.set(month_values[today_month-2]) #Set the default value to previous month -2 was used because 0 index
        #month_spin_box = tkinter.Spinbox(date_frame, from_=1, to=12, width=10, textvariable=self.month )
        month_combo_box = ttk.Combobox(date_frame, textvariable=self.month, width=10,)
        month_combo_box['values'] = month_values
        month_combo_box.grid(row=25, column=1, padx=5, pady=5)
        

        self.day = tkinter.IntVar()
        if self.month.get() in [month_values[3], month_values[5], month_values[8], month_values[10]]:
            self.day.set(30)                  
        elif self.month.get() == month_values[1] & self.year.get()%2==0:
             self.day.set(29)
        elif self.month.get() == month_values[1] & self.year.get()%2!=0:
             self.day.set(28)         
        else:
            self.day.set(31)
        #day_spin_box = tkinter.Spinbox(date_frame, from_=1, to=31, width=10, textvariable=self.day )
        self.day_combo_box = ttk.Combobox(date_frame, textvariable=self.day, width=10)
        self.day_combo_box['values'] = day_month_thirty_first  
        self.day_combo_box.grid(row=25, column=2, padx=5, pady=5)
        
    # def validate_day(self):

    #     def callback(self):
    #         if self.month.get() in [month_values[3], month_values[5], month_values[8], month_values[10]]:
    #             #self.day_combo_box.config
    #             day_combo_box.config('values') = day_month_thirty                
    #         elif self.month.get() == month_values[1] & self.year.get()%2==0:
    #             self.day_combo_box['values'] = list(day_month_feb.append([29]))
    #         elif self.month.get() == month_values[1] & self.year.get()%2!=0:
    #             self.day_combo_box = day_month_feb         
    #         else:
    #             self.day_combo_box['values'] = day_month_thirty_fisrt
    #     return callback
    
    def create_acct_status_checkbox(self, parentFrame):
        checkbox_frame = tkinter.Frame(parentFrame)
        checkbox_frame.grid(row=25, column=1, columnspan=1, sticky=E)

        self.acct_status_date_check = tkinter.BooleanVar()
        label_checkboxname = tkinter.Checkbutton(checkbox_frame, text='Use Date In Acct Status Date', variable=self.acct_status_date_check)
        label_checkboxname.grid(row=25, column=0, pady=5, padx=15, sticky=E)


    def create_display_canvas(self, parent_frame):
        dispaly_frame = Frame(parent_frame)
        dispaly_frame.grid(row=35, column=1, sticky=W+E)
        self.display_canvas = Canvas(dispaly_frame, height=125, width=700, borderwidth=4, background='white')
        self.display_canvas.grid(row=35, padx=5, pady=20, sticky=E)
        self.display_canvas_status_text=self.display_canvas.create_text(10, 10, text='Status:', anchor=W)
        self.display_status = self.display_canvas.create_text(50, 10, text='No file Choosen', anchor=W)

    def update_canvas(self):
        self.display_canvas.itemconfig(self.display_status, text=self.display.get())
        #self.display_canvas.itemconfig(self.display_canvas_status_text, text='Status:')
        #self.root.update()
        
    def validate_date(self):
        if self.year.get() in year_values and self.month.get() in month_values and self.day.get() in day_month_thirty_first:
            self.date_entered = str(self.year.get()) +"-"+ str(month_values.index(self.month.get())+1).zfill(2) + '-'+ str(self.day.get()).zfill(2)
            return TRUE
        else:
            self.date_entered = str(self.year.get()) +"-"+ self.month.get() + '-'+ str(self.day.get())
            return FALSE


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
                    self.display.set("Only Excel Workbook of type .xlsx and .xls can be selected")
                    messagebox.showinfo("Info", "Only Excel Workbook of type .xlsx and .xls can be selected")
                    return
                else:
                    print(filename)
                    self.selected_filename = filename
                    filenamebase_here = os.path.basename(filename)
                    
                    if self.display_canvas.gettags('message') != None:
                        self.display_canvas.delete('message')
                   
                    #self.create_display_canvas()
                    #self.display_canvas_status_text
                    #print(self.get_absolute_parent_path(filename))
                    self.display.set("File Selected")
                    self.filenamebase.set(filenamebase_here)
                    self.path_string.set(filename)
                    self.update_canvas()
                    
            except:
                messagebox.showerror('Invalid', 'Error loading excel file')
        return callback
        
    def validate(self)->bool:
        
        if self.selected_filename == '':
            print(self.selected_filename)
            print(self.subID_value.get())
            print("Validation Error", "No Excel File choosen yet. Please select a file")
            self.display.set("Validation Error! No Excel File choosen yet. Please select a file")
            messagebox.showwarning("Validation Error", "No Excel File choosen yet. Please select a file")              
            return FALSE
        elif self.subID_value.get() == '':
                
            print(self.selected_filename)
            print(self.subID_value.get())
            print("Validation Error", "Subscriber ID value not provided")
            self.display.set("Validation Error! Subscriber ID not provided")
            messagebox.showwarning("Validation Error", "Subscriber ID value not provided")
            return FALSE
        elif self.validate_date():
            #print(self.selected_filename)
            self.subID_provided = self.subID_value.get().strip()
            self.restrict_status_date = self.acct_status_date_check.get()
            print(self.subID_provided)
            print(self.date_entered)
            print("Validated")
            self.display.set("Validation completed")
            return TRUE

        else:
            self.display.set("Validation Error! Date {0} is invalid".format(self.date_entered))
            messagebox.showwarning("Validation Error", "Date {0} is invalid".format(self.date_entered))
            return FALSE
        

    def generate_text_fileclicked(self):

        def callback():
            if self.validate():
                print(self.selected_filename)
                try:
                    print(self.selected_filename)
                    excel_file_class_Obj = ExcelFile(self.selected_filename, self.subID_provided, self.date_entered, self.restrict_status_date)
                    print('-----------------------------------')
                    #print(type(excel_file_class_Obj.file_path))
                    print(excel_file_class_Obj.file_path)
                    print('Trying to read file')
                    self.display.set('Reading')
                    excel_file_class_Obj.read_excel_file(self.display)
                    self.display.set('Read file complete')
                    print('read file complete')
                    try:
                        print('-----------------------------------')
                        self.display.set('Trying to Write to file')
                        messages = excel_file_class_Obj.write_to_file(self.display)
                        
                        y=30
                        status_color = []
                        if messages != None:
                            for diction in messages:
                                for k, message in diction.items():
                                    self.display_canvas.create_text(10, y, text=message, anchor=W, tags='message', fill=k)
                                    status_color.append(k)
                                    y = y + 18
                            if 'green' in status_color:
                                self.display.set('Writing complete! Text file successfully generated')
                            else:
                                self.display.set('Error! No Text file was generated')
                        print(messages)
                    except os.error as werr:

                        messagebox.showerror('Invalid', 'Error writing to text file \n' +str(werr))                   
                    except:
                        self.display.set('Error! An error occured. ')
                        messagebox.showerror('Error', 'An error occurred while writing to text file ')
                except os.error as e:
                    messagebox.showerror('Invalid', 'Error reading excel file a '+ str(e))
                    print(os.error)
            else:
                return
        
        return callback


    
create = CreateApp()
create.app()