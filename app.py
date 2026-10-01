import streamlit as st
from datetime import datetime

# =====================================================
# CẤU HÌNH TRANG
# =====================================================

st.set_page_config(
    page_title="Tầm Nhìn Xanh - Trà Sữa",
    page_icon="🧋",
    layout="centered"
)

# =====================================================
# CSS - TRANG TRÍ GIAO DIỆN
# =====================================================

st.markdown("""
<style>

.main {
    background-color: #f8f8f8;
}

.title {
    text-align: center;
    color: #4F351F;
    font-size: 32px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #666666;
    font-size: 18px;
}

.total-box {
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    background-color: #F3E5AB;
    color: #4F351F;
    font-size: 24px;
    font-weight: bold;
}

.invoice-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #FFFDF5;
    border: 1px solid #DDDDDD;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HIỂN THỊ LOGO / HÌNH ĐẦU TRANG
# =====================================================

try:
    st.image(
        "logo.jpg",
        use_container_width=True
    )
except:
    st.warning(
        "⚠️ Không tìm thấy file logo.jpg. "
        "Hãy đặt logo.jpg cùng thư mục với app.py."
    )

# =====================================================
# TIÊU ĐỀ
# =====================================================

st.markdown(
    '<div class="title">🧋 QUẢN LÝ BILL TRÀ SỮA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'TẦM NHÌN XANH - SẢN PHẨM THỦ CÔNG TỪ TRE'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# =====================================================
# MENU TRÀ SỮA
# =====================================================

menu = {
    "Trà sữa truyền thống": 30000,
    "Trà sữa matcha": 35000,
    "Trà sữa socola": 35000,
    "Trà sữa khoai môn": 35000,
    "Trà sữa dâu": 35000,
    "Trà sữa thái xanh": 30000,
    "Trà sữa thái đỏ": 30000,
}

# =====================================================
# MENU TOPPING
# =====================================================

topping_menu = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Thạch trái cây": 5000,
    "Pudding trứng": 7000,
    "Kem cheese": 10000,
    "Thạch phô mai": 7000,
}

# =====================================================
# THÔNG TIN KHÁCH HÀNG
# =====================================================

st.subheader("👤 Thông tin khách hàng")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)

# =====================================================
# THÔNG TIN TRÀ SỮA
# =====================================================

st.subheader("🧋 Chọn trà sữa")

col1, col2 = st.columns(2)

with col1:

    loai_tra_sua = st.selectbox(
        "Loại trà sữa",
        list(menu.keys())
    )

    gia_tra_sua = menu[loai_tra_sua]

with col2:

    so_luong = st.number_input(
        "Số lượng ly",
        min_value=1,
        max_value=50,
        value=1,
        step=1
    )

# =====================================================
# ĐƯỜNG VÀ ĐÁ
# =====================================================

st.subheader("🍬 Tùy chọn thức uống")

col1, col2 = st.columns(2)

with col1:

    muc_duong = st.selectbox(
        "Mức độ đường",
        [
            "100%",
            "70%",
            "0%"
        ]
    )

with col2:

    muc_da = st.selectbox(
        "Mức độ đá",
        [
            "100%",
            "70%",
            "0%"
        ]
    )

# =====================================================
# TOPPING
# =====================================================

st.subheader("🍮 Chọn topping")

topping_chon = st.multiselect(
    "Topping",
    list(topping_menu.keys()),
    placeholder="Chọn một hoặc nhiều topping..."
)

# =====================================================
# SỐ LƯỢNG TOPPING
# =====================================================

topping_so_luong = {}

if topping_chon:

    st.write("**Số lượng topping cho mỗi ly:**")

    for topping in topping_chon:

        topping_so_luong[topping] = st.number_input(
            f"{topping} - {topping_menu[topping]:,} VNĐ",
            min_value=1,
            max_value=10,
            value=1,
            step=1,
            key=f"topping_{topping}"
        )

# =====================================================
# NÚT TÍNH BILL
# =====================================================

st.divider()

tinh_bill = st.button(
    "🧾 TÍNH BILL",
    use_container_width=True,
    type="primary"
)

# =====================================================
# XỬ LÝ TÍNH BILL
# =====================================================

if tinh_bill:

    if not ten_khach.strip():

        st.warning(
            "⚠️ Vui lòng nhập tên khách hàng!"
        )

    else:

        # ---------------------------------------------
        # TIỀN TRÀ SỮA
        # ---------------------------------------------

        tien_tra_sua = (
            gia_tra_sua * so_luong
        )

        # ---------------------------------------------
        # TIỀN TOPPING
        # ---------------------------------------------

        tien_topping = 0

        for topping in topping_chon:

            sl_topping = topping_so_luong[topping]

            tien_topping += (
                topping_menu[topping]
                * sl_topping
                * so_luong
            )

        # ---------------------------------------------
        # TỔNG TIỀN
        # ---------------------------------------------

        tong_tien = (
            tien_tra_sua
            + tien_topping
        )

        # ---------------------------------------------
        # LƯU SESSION
        # ---------------------------------------------

        st.session_state["da_tinh"] = True

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


# =====================================================
# HIỂN THỊ BILL
# =====================================================

if st.session_state.get("da_tinh", False):

    st.divider()

    st.subheader("🧾 THÔNG TIN ĐƠN HÀNG")

    # ---------------------------------------------
    # THÔNG TIN KHÁCH HÀNG
    # ---------------------------------------------

    st.write(
        f"👤 **Khách hàng:** "
        f"{st.session_state['ten_khach']}"
    )

    st.write(
        f"🧋 **Loại trà sữa:** "
        f"{st.session_state['loai_tra_sua']}"
    )

    st.write(
        f"💰 **Đơn giá:** "
        f"{st.session_state['gia_tra_sua']:,} VNĐ"
    )

    st.write(
        f"🔢 **Số lượng:** "
        f"{st.session_state['so_luong']} ly"
    )

    st.write(
        f"🍬 **Mức đường:** "
        f"{st.session_state['muc_duong']}"
    )

    st.write(
        f"🧊 **Mức đá:** "
        f"{st.session_state['muc_da']}"
    )

    # =================================================
    # TOPPING
    # =================================================

    st.write("🍮 **Topping:**")

    if st.session_state["topping_chon"]:

        for topping in st.session_state["topping_chon"]:

            sl = st.session_state[
                "topping_so_luong"
            ][topping]

            tong_sl = (
                sl
                * st.session_state["so_luong"]
            )

            thanh_tien = (
                topping_menu[topping]
                * tong_sl
            )

            st.write(
                f"- {topping}: "
                f"{tong_sl} phần × "
                f"{topping_menu[topping]:,} VNĐ "
                f"= **{thanh_tien:,} VNĐ**"
            )

    else:

        st.write("- Không có topping")

    st.divider()

    # =================================================
    # CHI TIẾT THANH TOÁN
    # =================================================

    st.write(
        f"🧋 Tiền trà sữa: "
        f"**{st.session_state['tien_tra_sua']:,} VNĐ**"
    )

    st.write(
        f"🍮 Tiền topping: "
        f"**{st.session_state['tien_topping']:,} VNĐ**"
    )

    st.markdown(
        f"""
        <div class="total-box">
        💵 TỔNG THANH TOÁN<br>
        {st.session_state['tong_tien']:,} VNĐ
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # =================================================
    # THANH TOÁN
    # =================================================

    thanh_toan = st.button(
        "💳 THANH TOÁN & XUẤT HÓA ĐƠN",
        use_container_width=True
    )

    if thanh_toan:

        # ---------------------------------------------
        # THỜI GIAN
        # ---------------------------------------------

        thoi_gian = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        # ---------------------------------------------
        # TẠO MÃ HÓA ĐƠN
        # ---------------------------------------------

        ma_hoa_don = datetime.now().strftime(
            "%Y%m%d%H%M%S"
        )

        # ---------------------------------------------
        # TẠO HÓA ĐƠN
        # ---------------------------------------------

        hoa_don = ""

        hoa_don += "=" * 50 + "\n"
        hoa_don += "              TẦM NHÌN XANH\n"
        hoa_don += "             HÓA ĐƠN TRÀ SỮA\n"
        hoa_don += "=" * 50 + "\n"

        hoa_don += (
            f"Mã hóa đơn: {ma_hoa_don}\n"
        )

        hoa_don += (
            f"Thời gian: {thoi_gian}\n"
        )

        hoa_don += (
            f"Khách hàng: "
            f"{st.session_state['ten_khach']}\n"
        )

        hoa_don += "-" * 50 + "\n"

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
            f"{st.session_state['so_luong']} ly\n"
        )

        hoa_don += (
            f"Mức đường: "
            f"{st.session_state['muc_duong']}\n"
        )

        hoa_don += (
            f"Mức đá: "
            f"{st.session_state['muc_da']}\n"
        )

        hoa_don += "-" * 50 + "\n"

        # ---------------------------------------------
        # TOPPING TRONG HÓA ĐƠN
        # ---------------------------------------------

        hoa_don += "TOPPING:\n"

        if st.session_state["topping_chon"]:

            for topping in st.session_state["topping_chon"]:

                sl = st.session_state[
                    "topping_so_luong"
                ][topping]

                tong_sl = (
                    sl
                    * st.session_state["so_luong"]
                )

                thanh_tien = (
                    topping_menu[topping]
                    * tong_sl
                )

                hoa_don += (
                    f"- {topping}: "
                    f"{tong_sl} phần × "
                    f"{topping_menu[topping]:,} VNĐ "
                    f"= {thanh_tien:,} VNĐ\n"
                )

        else:

            hoa_don += "- Không có topping\n"

        hoa_don += "-" * 50 + "\n"

        # ---------------------------------------------
        # TỔNG TIỀN
        # ---------------------------------------------

        hoa_don += (
            f"Tiền trà sữa: "
            f"{st.session_state['tien_tra_sua']:,} VNĐ\n"
        )

        hoa_don += (
            f"Tiền topping: "
            f"{st.session_state['tien_topping']:,} VNĐ\n"
        )

        hoa_don += "-" * 50 + "\n"

        hoa_don += (
            f"TỔNG THANH TOÁN: "
            f"{st.session_state['tong_tien']:,} VNĐ\n"
        )

        hoa_don += "=" * 50 + "\n"

        hoa_don += (
            "             CẢM ƠN QUÝ KHÁCH!\n"
        )

        hoa_don += (
            "              HẸN GẶP LẠI!\n"
        )

        hoa_don += "=" * 50 + "\n"

        # =================================================
        # THÔNG BÁO
        # =================================================

        st.success(
            "✅ THANH TOÁN THÀNH CÔNG!"
        )

        # =================================================
        # HIỂN THỊ HÓA ĐƠN
        # =================================================

        st.subheader("📄 HÓA ĐƠN")

        st.text_area(
            "Nội dung hóa đơn",
            hoa_don,
            height=450
        )

        # =================================================
        # NÚT TẢI HÓA ĐƠN
        # =================================================

        st.download_button(
            label="📥 TẢI HÓA ĐƠN",
            data=hoa_don.encode("utf-8"),
            file_name=(
                f"HoaDon_{ma_hoa_don}.txt"
            ),
            mime="text/plain",
            use_container_width=True
        )
