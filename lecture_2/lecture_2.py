# -*- coding: utf-8 -*-
# sans security training
#  locals() - поверне всі локальні змінні
# eval(), exec()
# talk about less
# shutil - робота з файлами пітоном


def main():
    with open("lec_2.txt", "a+") as file_1:
        while True:
            string_1 = raw_input("White something here \n")
            if string_1 != "quit":
                file_1.write(string_1 + '\n')
            else:
                string_2 = raw_input("Maybe you want to write something else??? (Y/N)" + '\n')
                if string_2 == "Y":
                    continue
                elif string_2 == "N":
                    exit()

if __name__ == "__main__":
    main()


# def main():
#     file_1 = open("lec_2.txt", "r")
#     with file_1 as f:
#         for line in f:
#             print line.strip("\n") + ' :)'
#
#     file_1.close()
#
#
# if __name__ == "__main__":
#     main()


# def main():
#     while True:
#         answer = raw_input("What is your name? \n")
#         if answer != "exit":
#             print answer
#         else:
#             exit()
#
# if __name__ == "__main__":
#     main()




# def func_1(**kwargs):
#     print(kwargs)
#
#
# def main():
#     string_1 = "2+3"
#     string_2 = 'print("HI")'
#
#     print (eval(string_1))
#
#     dic = locals().values()
#     for el in dic:
#         if type(el) == str:
#             print el
#     # print(eval(string_1))
#
# if __name__ == "__main__":
#     main()





# def func_1(**kwargs):
#     print(kwargs)
#
#
# def main():
#     arr = ['1', '2']
#     string_1 = "somme val"
#     string_2 = "some another val"
#     string_3 = str(2)
#     string_4 = """ I would like
#      to
#      write
#      #string
#      """
#     dic = locals().values()
#     for el in dic:
#         if type(el) == str:
#             print el
#
# if __name__ == "__main__":
#     main()


# def func_1(**kwargs):
#     print(kwargs)
#
#
# def main():
#     string_1 = "some value"
#     string_2 = 'some value'
#     string_3 = str(2)
#     string_4 = """" I would like
#     to
#     write
#     #string
#     """
#     arr = [string_1, string_2, string_3, string_4]
#
#     for el in arr:
#         print el
#
# if __name__ == "__main__":
#     main()






# def func_1(**kwargs):
#     print(kwargs)
#
#
# def main():
#     var_1 = "number"
#     print(repr(var_1))
#
# if __name__ == "__main__":
#     main()
