import tkinter as t

class TimerApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Timer App")

        
        self.seconds=0
        self.timer_running=False

        
        self.timer_label=t.Label(root,text="00:00",font=("Helvetica",48))
        self.timer_label.pack(pady=20)
        
       
        self.start_button=t.Button(root,text="start",command=self.start_timer)
        self.stop_button=t.Button(root,text="stop",command=self.stop_timer)
        self.start_button.pack(side=t.LEFT,padx=10)
        self.stop_button.pack(side=t.LEFT,padx=10)
        
        
    def start_timer(self):
        
        if not self.timer_running:
            self.timer_running=True
            self.update_timer()
            
    def stop_timer(self):
        self.timer_running=False
        
    def update_timer(self):
        
        if self.timer_running:
            self.seconds+=1
            minutes=self.seconds//60
            seconds=self.seconds%60
            time_str=f"(minutes:02):(seconds:02)"
            self.timer_label.config(text=time_str)
            self.root.after(1000,self.update_timer)
            
root=t.Tk()
app=TimerApp(root)
root.mainloop()
