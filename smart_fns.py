import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="SMART FNS - Plateforme Médicale", page_icon="🩺")

# عنوان المنصة
st.title("🩺 SMART FNS - Plateforme Médicale")
st.subheader("مرحباً بكم دكاترة المستقبل")

# رسالة ترحيبية
st.markdown("""
هذه المنصة مخصصة لمراجعة الحالات السريرية والأسئلة الطبية. 
يرجى اختيار القسم الذي ترغبون في مراجعته من القائمة الجانبية.
""")

# إضافة قسم تجريبي
st.divider()
st.write("### قائمة الأقسام المتاحة:")
st.button("1. مراجعة الحالات السريرية")
st.button("2. الأسئلة التخصصية (QCM)")

# تذييل الصفحة
st.sidebar.info("للتواصل مع الدكتورة: [أضيفي بريدك هنا]")