from file import khoitaofile
from quanlinhansu import nhap_thong_tin_nhan_su, xoa_nhan_su, cap_nhat_nhan_su, tim_kiem_nhan_su
def main():
    khoitaofile()
    while True:
        print("Vui lòng chọn chức năng quản lí nhân sự:")
        print("1. Nhập thông tin")
        print("2. Xóa thông tin")
        print("3. Cập nhật thông tin nhân sự")
        print("4. Tìm kiếm thông tin")
        print("5. Thoát chương trình")
        chuc_nang = input("Nhập lựa chọn: ")
        if chuc_nang == "1":
            nhap_thong_tin_nhan_su()
        elif chuc_nang == "2":
            xoa_nhan_su()
        elif chuc_nang == "3":
            cap_nhat_nhan_su()
        elif chuc_nang == "4":
            tim_kiem_nhan_su()
        elif chuc_nang == "5":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")
if __name__ == "__main__":
    main()

