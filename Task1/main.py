from core.manager import FinanceManager
#之後可能會加入GUI,或者將data另外save去database/excel
def main():
    app = FinanceManager()
    app.load_data()

    while True:
        print("\n" + "="*50)
        print("     個人智能記賬系統")
        print("="*50)
        print("1. 加入收入")
        print("2. 加入支出")
        print("3. 查看總結")
        print("4. 退出")
        choice = input("\n請輸入選擇 (1-4): ")

        if choice == "1":
            amount = float(input("金額: "))
            cat = input("類別 (e.g. 薪水、投資): ")
            app.add_transaction("現金錢包", amount, cat, True)
            print("✅ 收入已記錄！")
        elif choice == "2":
            amount = float(input("金額: "))
            cat = input("類別 (e.g. 飲食、交通): ")
            app.add_transaction("現金錢包", amount, cat, False)
            print("✅ 支出已記錄！")
        elif choice == "3":
            app.show_summary()
        elif choice == "4":
            print("👋 感謝使用！數據已自動儲存。")
            break
        else:
            print("❌ 輸入錯誤，請重試")

if __name__ == "__main__":
    main()