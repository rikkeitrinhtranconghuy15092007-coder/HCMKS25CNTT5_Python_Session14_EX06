# =====================================================
# HỆ THỐNG QUẢN LÝ ĐIỂM SỐ - BÀI TẬP TỔNG HỢP
# =====================================================

def find_student_index(book, student_id):
    """Hàm phụ trợ: Tìm index của học sinh theo ID (không phân biệt hoa thường)"""
    student_id = student_id.strip().upper()
    for idx, student in enumerate(book):
        if student["id"].upper() == student_id:
            return idx
    return -1


def display_grades(book):
    """Chức năng 1: Xem bảng điểm học sinh"""
    if not book:
        print("Danh sách học sinh trống!")
        return
    
    print("\n--- BẢNG ĐIỂM HỌC SINH ---")
    print(f"{'Mã SV':<6} | {'Tên Học Sinh':<20} | {'Điểm Toán':<9} | {'Điểm Anh':<9} | {'ĐTB':<6}")
    print("-" * 70)
    
    for student in book:
        math = student["info"][0]
        english = student["info"][1]
        average = (math + english) / 2
        print(f"{student['id']:<6} | {student['name']:<20} | {math:<9.1f} | {english:<9.1f} | {average:<6.2f}")
    
    print("-" * 70)


def add_student(book):
    """Chức năng 2: Thêm hồ sơ học sinh mới"""
    student_id = input("Nhập mã học sinh mới: ").strip()
    
    if find_student_index(book, student_id) != -1:
        print(f"Lỗi: Mã học sinh {student_id} đã tồn tại! Vui lòng nhập mã khác.")
        return
    
    name = input("Nhập tên học sinh: ").strip()
    
    try:
        math_score = float(input("Nhập điểm Toán: ").strip())
        english_score = float(input("Nhập điểm Anh: ").strip())
        
        # Tạo tuple info
        info_tuple = (math_score, english_score)
        
        new_student = {
            "id": student_id.upper(),
            "name": name,
            "info": info_tuple
        }
        
        book.append(new_student)
        print(f"Thành công: Đã thêm học sinh {student_id} vào hệ thống!")
        
    except ValueError:
        print("Lỗi: Điểm số phải là số thực hợp lệ!")


def update_scores(book):
    """Chức năng 3: Cập nhật điểm số (Xử lý Tuple immutable)"""
    student_id = input("Nhập mã học sinh cần cập nhật: ").strip()
    idx = find_student_index(book, student_id)
    
    if idx == -1:
        print(f"Lỗi: Không tìm thấy học sinh có mã {student_id}!")
        return
    
    try:
        math_new = float(input("Nhập điểm Toán mới: ").strip())
        english_new = float(input("Nhập điểm Anh mới: ").strip())
        
        # Tạo tuple mới để ghi đè (vì tuple không thể thay đổi trực tiếp)
        new_info = (math_new, english_new)
        book[idx]["info"] = new_info
        
        print(f"Thành công: Đã cập nhật điểm cho học sinh {student_id}!")
        
    except ValueError:
        print("Lỗi: Điểm số phải là số thực hợp lệ!")


def delete_student(book):
    """Chức năng 4: Xóa hồ sơ học sinh"""
    student_id = input("Nhập mã học sinh cần xóa: ").strip()
    idx = find_student_index(book, student_id)
    
    if idx == -1:
        print(f"Lỗi: Không tìm thấy học sinh có mã {student_id}!")
        return
    
    deleted_name = book[idx]["name"]
    del book[idx]
    print(f"Thành công: Đã xóa hồ sơ học sinh {student_id} - {deleted_name} khỏi hệ thống!")


def main():
    """Hàm chính: Điều hướng Menu"""
    # Dữ liệu mẫu
    grade_book = [
        {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
        {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
    ]
    
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===")
        print("1. Xem bảng điểm học sinh")
        print("2. Thêm hồ sơ học sinh mới")
        print("3. Cập nhật điểm số")
        print("4. Xóa hồ sơ học sinh")
        print("5. Thoát chương trình")
        print("=" * 32)
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            display_grades(grade_book)
        elif choice == "2":
            add_student(grade_book)
        elif choice == "3":
            update_scores(grade_book)
        elif choice == "4":
            delete_student(grade_book)
        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 5.")


if __name__ == "__main__":
    main()