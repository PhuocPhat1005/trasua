import streamlit as st

st.title('Trà Sữa COTAI')

radio = st.radio(label = 'Kích cỡ', options = ['Nhỏ(30K)', 'Vừa(40K)', 'Lớn(50K)'], horizontal = True)

st.write('Thêm')

col1, col2, col3, col4 = st.columns(4)

with col1:
    choose1 = st.checkbox('Sữa(5K)')
with col2:
    choose2 = st.checkbox('Cà phê(8K)')
with col3:
    choose3 = st.checkbox('Kem(10K)')
with col4:
    choose4 = st.checkbox('Trứng(15K)')

options = st.multiselect('Topping', ['Trân châu trắng (5K)', 'Trân châu đen (5K)', 'Thạch rau câu (6K)', 'Vải (7K)', 'Nhãn (8K)', 'Đào (10K)'], ['Trân châu trắng (5K)', 'Vải (7K)'], key = str)

number = st.number_input('Số lượng', min_value = 0, max_value = None, value = "min", step = 1)

text_area = st.text_area('Ghi chú', 'Ít đá, nhiều sữa, shipper đẹp trai')

if st.button('Đặt hàng'):
    if radio == 'Nhỏ(30K)':
        st.write('Cỡ Nhỏ')
        size = float(30)
    elif radio == 'Vừa(40K)':
        st.write('Cỡ Vừa')
        size = float(40)
    elif radio == 'Lớn(50K)':
        st.write('Cỡ Lớn')
        size = float(50)
        
    str = 'Thêm: '

    addMoney = 0
    if choose1:
        str += 'Sữa,'
        addMoney += 5
    if choose2:
        str += 'Cà phê,'
        addMoney += 8
    if choose3:
        str += 'Kem,'
        addMoney += 10
    if choose4:
        str += 'Trứng,'
        addMoney += 15
        
    st.write(str.rstrip(","))
    
    toppingMoney = 0
    num = len(options)
    for i in range(0, num):
        if options[i] == 'Trân châu trắng (5K)':
            toppingMoney += 5
        elif options[i] == 'Trân châu đen (5K)':
            toppingMoney += 5
        elif options[i] == 'Thạch rau câu (6K)':
            toppingMoney += 6
        elif options[i] == 'Vải (7K)':
            toppingMoney += 7
        elif options[i] == 'Nhãn (8K)':
            toppingMoney += 8
        elif options[i] == 'Đào (10K)':
            toppingMoney += 10

    st.write('Topping: ', options, type(options))
    
    st.write('Số lượng: ', number, type(number))

    st.write('Ghi chú: ', text_area, type(text_area))

    result = (size + addMoney + toppingMoney) * number

    st.write(f'Thành tiền: {result}')
    
