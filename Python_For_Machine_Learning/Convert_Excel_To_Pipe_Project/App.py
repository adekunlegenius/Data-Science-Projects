import tkinter  
from tkinter.constants import *
import os
from tkinter import filedialog
from tkinter import messagebox

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
        self.path_string.set('No file choosen')

        entry = tkinter.Entry(center_frame_obj, textvariable=self.path_string, state='readonly')
        entry.grid(row=10,  column=1, padx=5, pady=5, sticky=W+E)

        label = tkinter.Label(center_frame_obj, text='Subscriber ID:')
        label.grid(row=15, column=0, pady=5, padx=5)

        entry_sub_id = tkinter.Entry(center_frame_obj, width=110 )
        entry_sub_id.grid(row=15, column=1,  padx=5, pady=5)

        label_filename = tkinter.Label(center_frame_obj, text='File Selected:')
        label_filename.grid(row=20, column=0, pady=5, padx=5)

        self.filenamebase= tkinter.StringVar()
        self.filenamebase.set('No file selected')

        entry = tkinter.Entry(center_frame_obj, textvariable=self.filenamebase, state='readonly')
        entry.grid(row=20,  column=1, padx=5, pady=5, sticky=W+E)

        button_gen = tkinter.Button(center_frame_obj, text='Generate Text File',  border=2)
        button_gen.grid(row=25,  column=1, pady=2, padx=2, sticky=N+E)

    def choose_file_clicked(self):
        global filename
        def callback():
            try:
                filename = filedialog.askopenfilename(defaultextension='.xlsx', filetypes=[('All Files', '*.*'), ("Excel Work Book", "*.xlsx"), ("Excel 97-2003 Workbook", "*.xls")])

                if filename == "":
                    filename = None
                    return
                    
                elif filename.split('.')[-1] not in ['xlsx', 'xls']:
                    messagebox.showinfo("Info", "Only Excel Workbook of type .xlsx and .xls can be selected")
                    return
                else:
                    print(filename)
                    filenamebase_here = os.path.basename(filename)
                    
                    # path_list = filename.split('/')
                    # path_list.remove(path_list[-1])
                    # print('/'.join(path_list))
                    #print(path_list)

                    print(self.get_absolute_parent_path(filename))
                    
                    self.filenamebase.set(filenamebase_here)
                    self.path_string.set(filename)
            except:
                messagebox.showerror('Invalid', 'Error loading excel file')
        return callback

    def get_absolute_parent_path(self, path_name, sep='/')->str:
        
        path_list = path_name.split(sep)
        path_list.remove(path_list[-1])
        return sep.join(path_list)
        


create = CreateApp()
create.app()