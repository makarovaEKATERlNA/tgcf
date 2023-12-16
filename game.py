class Button():
    cli=0
    def click(self):
        self.cli+=1
    def click_count(self):
        print(self.cli)
    def click_reset(self):
        self.cli=0
n=len(input())
button1=Button()
for i in range(n):
    button1.click()
button1.click_count()
button1.click_reset()
print(button1.cli)
