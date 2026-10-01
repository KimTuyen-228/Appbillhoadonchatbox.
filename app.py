import streamlit as st
from datetime import datetime
import io

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Bill Trà Sữa",
    page_icon="🧋",
    layout="centered"
)

# =========================
# DỮ LIỆU MENU
# =========================
menu = {
    "Trà sữa truyền thống": 30000,
    "Trà sữa matcha": 35000,
    "Trà sữa socola": 35000,
    "Trà sữa khoai môn": 35000,
    "Trà sữa dâu": 35000,
    "Trà sữa thái xanh": 30000,
    "Trà sữa thái đỏ": 30000,
}

topping_menu = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Thạch trái cây": 5000,
    "Pudding trứng": 7000,
    "Kem cheese": 10000,
    "Thạch phô mai": 7000,
}

# =========================
# TIÊU ĐỀ
# =========================
st.title("🧋 QUẢN LÝ BILL TRÀ SỮA")
st.markdown("### Nhập thông tin đơn hàng")

# =========================
# THÔNG TIN KHÁCH HÀNG
# =========================
ten_khach = st.text_input(
    "👤 Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)

st.divider()

# =========================
# CHỌN TRÀ SỮA
# =========================
st.subheader("🧋 Thông tin trà sữa")

loai_tra_sua = st.selectbox(
    "Chọn loại trà sữa",
    list(menu.keys())
)

gia_tra_sua = menu[loai_tra_sua]

so_luong = st.number_input(
    "Số lượng",
    min_value=1,
    max_value=50,
    value=1,
    step=1
)

# =========================
# ĐƯỜNG VÀ ĐÁ
# =========================
col1, col2 = st.columns(2)

with col1:
    muc_duong = st.selectbox(
        "🍬 Mức độ đường",
        ["100%", "70%", "0%"]
    )

with col2:
    muc_da = st.selectbox(
        "🧊 Mức độ đá",
        ["100%", "70%", "0%"]
    )

# =========================
# TOPPING
# =========================
st.subheader("🍮 Topping")

topping_chon = st.multiselect(
    "Chọn topping",
    list(topping_menu.keys())
)

# Nhập số lượng cho từng topping
topping_so_luong = {}

if topping_chon:
    st.write("Số lượng topping:")

    for topping in topping_chon:
        topping_so_luong[topping] = st.number_input(
            f"{topping} - {topping_menu[topping]:,}đ",
            min_value=1,
            max_value=10,
            value=1,
            step=1,
            key=f"sl_{topping}"
        )

# =========================
# NÚT XEM ĐƠN HÀNG
# =========================
st.divider()

if st.button("🛒 XEM ĐƠN HÀNG", use_container_width=True):

    if not ten_khach.strip():
        st.warning("⚠️ Vui lòng nhập tên khách hàng!")
    else:

        # Tính tiền trà sữa
        tien_tra_sua = gia_tra_sua * so_luong

        # Tính tiền topping
        tien_topping = 0

        for topping in topping_chon:
            tien_topping += (
                topping_menu[topping] *
                topping_so_luong[topping] *
                so_luong
            )

        # Tổng tiền
        tong_tien = tien_tra_sua + tien_topping

        # Lưu vào session
        st.session_state["ten_khach"] = ten_khach
        st.session_state["loai_tra_sua"] = loai_tra_sua
        st.session_state["gia_tra_sua"] = gia_tra_sua
        st.session_state["so_luong"] = so_luong
        st.session_state["muc_duong"] = muc_duong
        st.session_state["muc_da"] = muc_da
        st.session_state["topping_chon"] = topping_chon
        st.session_state["topping_so_luong"] = topping_so_luong
        st.session_state["tien_tra_sua"] = tien_tra_sua
        st.session_state["tien_topping"] = tien_topping
        st.session_state["tong_tien"] = tong_tien
        st.session_state["da_xem"] = True


# =========================
# HIỂN THỊ BILL
# =========================
if st.session_state.get("da_xem", False):

    st.divider()
    st.subheader("🧾 THÔNG TIN ĐƠN HÀNG")

    st.write(
        f"**👤 Khách hàng:** "
        f"{st.session_state['ten_khach']}"
    )

    st.write(
        f"**🧋 Trà sữa:** "
        f"{st.session_state['loai_tra_sua']}"
    )

    st.write(
        f"**💰 Đơn giá:** "
        f"{st.session_state['gia_tra_sua']:,} VNĐ"
    )

    st.write(
        f"**🔢 Số lượng:** "
        f"{st.session_state['so_luong']}"
    )

    st.write(
        f"**🍬 Đường:** "
        f"{st.session_state['muc_duong']}"
    )

    st.write(
        f"**🧊 Đá:** "
        f"{st.session_state['muc_da']}"
    )

    # Hiển thị topping
    if st.session_state["topping_chon"]:

        st.write("**🍮 Topping:**")

        for topping in st.session_state["topping_chon"]:

            sl = st.session_state["topping_so_luong"][topping]

            st.write(
                f"- {topping}: "
                f"{sl} phần × "
                f"{st.session_state['so_luong']} ly "
                f"= {sl * st.session_state['so_luong']} phần"
            )

    else:
        st.write("**🍮 Topping:** Không có")

    st.divider()

    # Chi tiết tiền
    st.write(
        f"Tiền trà sữa: "
        f"**{st.session_state['tien_tra_sua']:,} VNĐ**"
    )

    st.write(
        f"Tiền topping: "
        f"**{st.session_state['tien_topping']:,} VNĐ**"
    )

    st.success(
        f"💵 TỔNG THANH TOÁN: "
        f"{st.session_state['tong_tien']:,} VNĐ"
    )

    # =========================
    # THANH TOÁN
    # =========================
    st.divider()

    if st.button(
        "💳 THANH TOÁN & XUẤT HÓA ĐƠN",
        use_container_width=True
    ):

        thoi_gian = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        # Tạo nội dung hóa đơn
        hoa_don = ""

        hoa_don += "=" * 45 + "\n"
        hoa_don += "          HÓA ĐƠN TRÀ SỮA\n"
        hoa_don += "=" * 45 + "\n"

        hoa_don += f"Thời gian: {thoi_gian}\n"
        hoa_don += (
            f"Khách hàng: "
            f"{st.session_state['ten_khach']}\n"
        )

        hoa_don += "-" * 45 + "\n"

        hoa_don += (
            f"Trà sữa: "
            f"{st.session_state['loai_tra_sua']}\n"
        )

        hoa_don += (
            f"Đơn giá: "
            f"{st.session_state['gia_tra_sua']:,} VNĐ\n"
        )

        hoa_don += (
            f"Số lượng: "
            f"{st.session_state['so_luong']}\n"
        )

        hoa_don += (
            f"Mức đường: "
            f"{st.session_state['muc_duong']}\n"
        )

        hoa_don += (
            f"Mức đá: "
            f"{st.session_state['muc_da']}\n"
        )

        hoa_don += "-" * 45 + "\n"

        if st.session_state["topping_chon"]:

            hoa_don += "TOPPING:\n"

            for topping in st.session_state["topping_chon"]:

                sl = st.session_state[
                    "topping_so_luong"
                ][topping]

                thanh_tien = (
                    topping_menu[topping]
                    * sl
                    * st.session_state["so_luong"]
                )

                hoa_don += (
                    f"- {topping}: "
                    f"{sl * st.session_state['so_luong']} phần "
                    f"x {topping_menu[topping]:,} VNĐ "
                    f"= {thanh_tien:,} VNĐ\n"
                )

        else:
            hoa_don += "TOPPING: Không có\n"

        hoa_don += "-" * 45 + "\n"

        hoa_don += (
            f"Tiền trà sữa: "
            f"{st.session_state['tien_tra_sua']:,} VNĐ\n"
        )

        hoa_don += (
            f"Tiền topping: "
            f"{st.session_state['tien_topping']:,} VNĐ\n"
        )

        hoa_don += "-" * 45 + "\n"

        hoa_don += (
            f"TỔNG THANH TOÁN: "
            f"{st.session_state['tong_tien']:,} VNĐ\n"
        )

        hoa_don += "=" * 45 + "\n"
        hoa_don += "       CẢM ƠN QUÝ KHÁCH!\n"
        hoa_don += "=" * 45 + "\n"

        # Thông báo thanh toán
        st.success("✅ Thanh toán thành công!")

        # Hiển thị hóa đơn
        st.text_area(
            "🧾 Hóa đơn",
            hoa_don,
            height=400
        )

        # Nút tải hóa đơn
        st.download_button(
            label="📥 TẢI HÓA ĐƠN",
            data=hoa_don,
            file_name=(
                f"hoa_don_"
                f"{st.session_state['ten_khach']}_"
                f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            ),
            mime="text/plain",
            use_container_width=True
        )
