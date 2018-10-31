import math
from time import sleep
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime as dt


def logininvoice():
    browser.find_element_by_id('account-email').send_keys(greenusername_input)
    browser.find_element_by_id('account-password').send_keys(greenpassword_input)
    browser.find_element_by_class_name('form-action').click()
    greeninvoice()

def checklogininvoice():
    if browser.current_url == "https://www.greeninvoice.co.il/app/account/login?rurl=https%3A%2F%2Fwww.greeninvoice.co.il%2Fapp%2Fdocuments%2Fnew#type=100":
        logininvoice()
    else:
        greeninvoice()

def loginyalla():
    browser.find_element_by_name('email').send_keys(greenusername_input)
    browser.find_element_by_name('password').send_keys(yallapassword_input)
    browser.find_element_by_name('password').send_keys(Keys.ENTER)
    sleep(1.5)
    if(browser.current_url == "http://www.yalla.co.il/login"):
        showproblem("Yalla Username or password incorrect")
    else:
        yalla()


def greeninvoice():
    sleep(2)

    def normal():
        sleep(0.3)
        browser.find_element_by_xpath(
            '//*[@id="income-rows"]/tbody[1]/tr/td[1]/div/div/input').click()
        element = browser.find_element_by_xpath('//*[@id="income-rows"]/tbody[1]/tr/td[1]/div/div/input')
        browser.execute_script("arguments[0].click();", element)
        browser.find_element_by_xpath(
            '//*[@id="income-rows"]/tbody[1]/tr/td[1]/div/div/input').send_keys(
            Keys.DOWN)
        browser.find_element_by_xpath(
            '//*[@id="income-rows"]/tbody[1]/tr/td[1]/div/div/input').send_keys(
            Keys.ENTER)

    def selector():
        browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/main/section[3]/form/fieldset/ul/li[1]/div/div/input').click()
        browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/main/section[3]/form/fieldset/ul/li[1]/div/div/input').send_keys(Keys.DOWN)
        browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/main/section[3]/form/fieldset/ul/li[1]/div/div/input').send_keys(Keys.DOWN)
        browser.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/main/section[3]/form/fieldset/ul/li[1]/div/div/input').send_keys(Keys.ENTER)

    def notnormal():
     sleep(0.3)
     browser.find_element_by_xpath(
        '//*[@id="income-rows"]/tbody[1]/tr/td[1]/div/div/input').click()
     browser.find_element_by_xpath(
        '//*[@id="income-rows"]/tbody[1]/tr/td[1]/div/div/input').send_keys(
        Keys.UP)
     browser.find_element_by_xpath(
        '//*[@id="income-rows"]/tbody[1]/tr/td[1]/div/div/input').send_keys(
        Keys.ENTER)

    if browser.current_url == "https://www.greeninvoice.co.il/app/documents/new#type=100":
        sleep(1)
        selector()
        normal()
        helper = 1
        positive = 0
        for y in range(count):
            for h in range(0,25):
               if(itemdesc[y] == veglist[h]):
                  positive = 1
            if(helper == 2 and positive == 0):
                notnormal()
                helper=1
            if(helper == 2 and positive == 1):
                notnormal()
                helper=1
            if (helper == 1 and positive == 1):
                normal()
                helper = 2
            browser.find_element_by_id('document-income-quantity').clear()
            browser.find_element_by_id('document-income-quantity').send_keys(amount[y])
            browser.find_element_by_id('document-income-price').send_keys(priceper[y])
            browser.find_element_by_id('document-income-description').send_keys(itemdesc[y])
            browser.find_element_by_css_selector(".add-income-row").click()
            positive = 0
        browser.find_element_by_class_name('input').send_keys(email)
    else:
        print(browser.current_url)


def yalla():
    sleep(2)
    global count
    count =(len(browser.find_elements_by_class_name('flyingCart'))-8)/8
    count = math.floor(count)
    def xpathhelper(param, variable, number):
        xpath = "/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td[2]/table/tbody//tr["
        xpath += str(variable)
        xpath += "]/td["
        xpath += str(number)
        xpath += "]"
        return xpath
    lst = range(2, count+2)
    global email
    email=browser.find_element_by_xpath(
        '/html/body/table[2]/tbody/tr/td/form/table[4]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]').text
    for x in lst:
          itemdesc.append(browser.find_element_by_xpath(xpathhelper('/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td[2]/table/tbody//tr[x]/td[2]', x, 2)).text)
          priceper.append(browser.find_element_by_xpath(xpathhelper('/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td[2]/table/tbody//tr[x]/td[5]', x, 5)).text)
          amount.append(browser.find_element_by_xpath(xpathhelper('/html/body/table[2]/tbody/tr/td/form/table[1]/tbody/tr[2]/td[2]/table/tbody//tr[x]/td[6]', x, 6)).text)
    sleep(1)
    browser.get('https://www.greeninvoice.co.il/app/documents/new#type=100')
    logininvoice()


def mainsoftware():
    global root
    root = Tk()
    var = StringVar()
    root.title("Welcome")
    root.configure(background='grey')
    root.resizable(0,0)
    root.geometry('510x530')
    label_0 = Label(root, text="FillFormAuto", width=16, bg="grey",font=("bold", 20),relief="ridge")
    label_0.place(x=125, y=33)

    label_1 = Label(root, text="Yalla Username", width=16, font=("bold", 10), relief="ridge")
    label_1.place(x=68, y=130)
    yallausername_entry = Entry(root, bg="lightgrey", width=30,relief="sunken")
    yallausername_entry.place(x=240, y=130)

    label_2 = Label(root, text="Yalla Password", width=16, font=("bold", 10), relief="ridge")
    label_2.place(x=68, y=180)
    yallapassword_entry = Entry(root, bg="lightgrey", width=30,relief="sunken")
    yallapassword_entry.place(x=240, y=180)

    label_3 = Label(root, text="Green Username", width=16, font=("bold", 10), relief="ridge")
    label_3.place(x=68, y=230)
    greenusername_entry = Entry(root, bg="lightgrey", width=30,relief="sunken")
    greenusername_entry.place(x=240, y=230)

    label_4 = Label(root, text="Green Password", width=16, font=("bold", 10), relief="ridge")
    label_4.place(x=68, y=280)
    greenpassword_entry = Entry(root, bg="lightgrey", width=30,relief="sunken")
    greenpassword_entry.place(x=240, y=280)

    label_url = Label(root, text="Yalla URL", width=15, font=("bold", 10), relief="ridge")
    label_url.place(x=15, y=380)
    entry_url = Entry(root, width=53, bg="lightgrey",relief="sunken")
    entry_url.place(x=170, y=381)

    labeltimeleft = Label(root, text="Days left:",bg="grey", width=10, font=("arial", 10), relief="flat")
    labeltimeleft.place(x=135, y=92)
    labeltimeleft = Label(root, textvariable=var, width=3,bg="grey", font=("arial", 10), relief="flat")
    labeltimeleft.place(x=240, y=92)

    def checkemptyinputs():
        global url
        global greenusername_input
        global greenpassword_input
        global yallausername_input
        global yallapassword_input
        url = entry_url.get()
        greenusername_input = greenusername_entry.get()
        greenpassword_input = greenpassword_entry.get()
        yallausername_input = yallausername_entry.get()
        yallapassword_input = yallapassword_entry.get()

        if (greenusername_input == "" or greenpassword_input == "" or yallausername_input == "" or
                yallapassword_input == ""):
            showproblem("Please Fill All")
        else:
            projectjob()

    var.set(viewdaysleft().days)
    clickButton = Button(root, height=3,text="Submit",width=20,relief="raised",  command=checkemptyinputs, bg="green")
    clickButton.place(x=183 , y=430)


    root.mainloop()

def projectjob():

    global browser
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()
    global amount
    amount = []
    global priceper
    priceper = []
    global itemdesc
    itemdesc = []
    global veglist
    veglist = ['אפרסמון מובחר 1 ק"ג'
    ,'תפוז מובחר 1 ק"ג', 'אפרסק מובחר 1 ק"ג','לימון מובחר 1 ק"ג','צרור נענע','אגס מובחר 1 ק"ג'
        ,'קלמנטינה מובחרת 1 ק"ג','עגבניה מובחר 1 ק"ג','מלפפון מובחר 1 ק"ג','אגס מובחר 1 ק"ג','פלפל אדום מובחר 1 ק"ג',
               'בננה מובחר 1 ק"ג','תפוח עץ סמיט מובחר 1 ק"ג','תמר מגהול מובחר 1 ק"ג','פלפל כתום מובחר 1 ק"ג',
               'תפוח אדום מובחר 1 ק"ג','מלון מובחר שלם','פלפל צהוב מובחר 1 ק"ג','ענבים ירוקים מובחר 1 ק"ג','עגבניית שרי מובחר 1 ק"ג',
               'אבוקדו מובחר 1 ק"ג','בצל מובחר 1 ק"ג','גזר מובחר 1 ק"ג','תמר מגהול מובחר 5 ק"ג','תות שדה ארוז 0.5 ק"ג','חסה אייסברג בקופסא']
    loginyalla()

def showproblem(problem):
    toplevel = Toplevel()
    toplevel.resizable(0,0)
    toplevel.geometry('400x200')
    label1 = Label(toplevel, text=problem, height=50,bg="lightblue", width=100, font=("bold", 15))
    label1.pack()


def Liecensewindowcheck():
    def checkifemptykey():
        global limitedkey
        limitedkey = Liecenseentry.get()
        if (len(limitedkey) != 32):
            showproblem("Please Enter a Valid Key")
        else:
            checkkey()

    def storekey(key, days, numbertodel, activate):
        x=numbertodel
        def deletekey(x):
            ref = firebase()
            ref.child(x).set("Activated")

        deletekey(x)
        dataset = [key, days, activate]
        outputFile = 'test.data'
        fw = open(outputFile, 'wb')
        pickle.dump(dataset, fw)
        fw.close()

    def checkkey():
        bypass = 0
        activate = viewactivate()
        ref = firebase()
        check = ref.get()
        for x in range(1, 51):
            if (str(check[x]) == str(limitedkey)):
                activate = "1"
                bypass = str(x)
        def handlercheckekey(number):
            if(activate == "1"):
                showproblem("Activate Program! Enjoy!")
                storekey(limitedkey, dt.datetime.now() + dt.timedelta(days=30), bypass, "1")
                root1.destroy()
                mainsoftware()
            if(activate != "1"):
                showproblem("Wrong Activate Code")

        handlercheckekey(bypass)
    root1 = Tk()
    root1.title("License")
    root1.configure(background='lightblue')
    root1.resizable(0,0)
    root1.geometry('420x250')
    label22 = Label(root1, text="Paste your Liecense Key here", width=30, font=("bold", 10), relief="ridge")
    label22.place(x=90, y=50)
    Liecenseentry = Entry(root1, bg="grey", width=55,relief="sunken")
    Liecenseentry.place(x=42, y=110)
    checkkeyButton = Button(root1, text="Submit",width=15,relief="raised",  command=checkifemptykey, bg="green")
    checkkeyButton.place(x=150,y=200)

    root1.mainloop()

def viewkey():
    inputFile = 'test.data'
    fd = open(inputFile, 'rb')
    dataset = pickle.load(fd)
    dataset = str(dataset[0])
    return dataset[0]

def viewdaysleft():
    inputFile = 'test.data'
    fd = open(inputFile, 'rb')
    dataset = pickle.load(fd)
    timetoend = dataset[1]
    first = dataset[0]
    assist = timetoend - dt.datetime.now()
    if (dt.datetime.now() < timetoend):
        dataset = [first, timetoend, "1"]
        outputFile = 'test.data'
        fw = open(outputFile, 'wb')
        pickle.dump(dataset, fw)
        fw.close()

    else:
        dataset = [first, timetoend, "0"]
        outputFile = 'test.data'
        fw = open(outputFile, 'wb')
        pickle.dump(dataset, fw)
        fw.close()
    return assist

def viewactivate():
    inputFile = 'test.data'
    fd = open(inputFile, 'rb')
    dataset = pickle.load(fd)
    assist = str(dataset[2])
    return assist

def mainfunction():
    viewdaysleft()
    global activate
    activate = viewactivate()
    cred = credentials.Certificate('./Servicesdk.json')
    default_app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://liecense-453de.firebaseio.com'})
    global activeday
    activeday = viewdaysleft()
    if(activate == "1"):
        mainsoftware()
    else:
        Liecensewindowcheck()

def firebase():
    ref = db.reference(path='Database').child("Keys")
    return ref

mainfunction()
