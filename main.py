import flet as ft

def main(page: ft.Page):
    page.title = "الحاسبة الصحية الشاملة"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.window.width = 390
    page.window.height = 700
    page.scroll = "auto"
    page.padding = 20
    page.window.resizable = False

    # ---------- الصفحة الرئيسية ----------
    def home_page(e=None):
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    ft.Text("🏋️‍♂️ الحاسبة الصحية الشاملة", size=20, weight=ft.FontWeight.BOLD,font_family="Courier New"),
                    ft.Row(
                        [
                            ft.ElevatedButton("⚖️ حساب الوزن المثالي", on_click=lambda ev: ideal_weight_page()),
                            ft.ElevatedButton("⚖️ حساب BMI", on_click=lambda ev: bmi_page()),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton("🍗 حساب احتياج البروتين", on_click=lambda ev: protein_page()),
                            ft.ElevatedButton("🍞 حساب احتياج الكربوهيدرات", on_click=lambda ev: carbs_page()),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton("🥑 حساب احتياج الدهون", on_click=lambda ev: fats_page()),
                            ft.ElevatedButton("💧 حساب كمية الماء", on_click=lambda ev: water_page()),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton("🥦 حساب الألياف اليومية", on_click=lambda ev: fiber_page()),
                            ft.ElevatedButton("😴 حساب ساعات النوم", on_click=lambda ev: sleep_page()),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10
                    ),
             # --------- coprighting developper ---------- 

                    ft.Text("DEVELOPPED BY KHIRE_EDDINE_RJ",size=18, weight=ft.FontWeight.BOLD,font_family="Courier New")
                        
                ],
                spacing=12,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        page.update()

    # ---------- صفحة الوزن المثالي (مثال - يمكنك تعديل الصيغة لديك) ----------
    def ideal_weight_page():
        page.controls.clear()
        height = ft.TextField(label="الطول (سم)", width=170)
        gender = ft.Dropdown(
            label="الجنس",
            width=170,
            options=[ft.dropdown.Option("ذكر"), ft.dropdown.Option("أنثى")],
        )
        result = ft.Text()

        def calc(ev):
            try:
                h = float(height.value)
                if gender.value == "ذكر":
                    ideal = (h - 100) - ((h - 100) * 0.1)  # مثال صيغة بسيطة
                else:
                    ideal = (h - 100) - ((h - 100) * 0.15)
                result.value = f"📌 الوزن المثالي التقريبي: {ideal:.1f} كغ"
            except Exception:
                result.value = "⚠️ الرجاء إدخال الطول واختيار الجنس بشكل صحيح."
            page.update()

        page.add(
            ft.Column(
                [
                    ft.Text("⚖️ حساب الوزن المثالي", size=22, weight=ft.FontWeight.BOLD),
                    ft.Row([height, gender], spacing=10),
                    ft.ElevatedButton("احسب", on_click=calc),
                    result,
                    ft.TextButton("⬅️ رجوع", on_click=lambda e: home_page()),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8
            )
        )
        page.update()

    # ---------- صفحة BMI (مثال) ----------
    def bmi_page():
        page.controls.clear()
        weight = ft.TextField(label="الوزن (كغ)", width=150)
        height = ft.TextField(label="الطول (سم)", width=150)
        result = ft.Text()

        def calc(ev):
            try:
                w = float(weight.value)
                h_cm = float(height.value)
                h_m = h_cm / 100.0
                bmi = w / (h_m * h_m)
                if bmi < 18.5:
                    status = "نحافة"
                elif bmi < 25:
                    status = "طبيعي"
                elif bmi < 30:
                    status = "زيادة وزن"
                else:
                    status = "سمنة"
                result.value = f"BMI = {bmi:.1f} → {status}"
            except Exception:
                result.value = "⚠️ الرجاء إدخال قيم صحيحة للوزن والطول."
            page.update()

        page.add(
            ft.Column(
                [
                    ft.Text("📊 حساب مؤشر كتلة الجسم (BMI)", size=22, weight=ft.FontWeight.BOLD),
                    ft.Row([weight, height], spacing=10),
                    ft.ElevatedButton("احسب", on_click=calc),
                    result,
                    ft.TextButton("⬅️ رجوع", on_click=lambda e: home_page()),
                ],
                spacing=8,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        page.update()

    # ---------- صفحة البروتين ----------
    def protein_page():
        page.controls.clear()
        weight = ft.TextField(label="الوزن (كغ)", width=200)
        level = ft.Dropdown(
            label="مستوى النشاط",
            width=200,
            options=[
                ft.dropdown.Option("عادي"),
                ft.dropdown.Option("رياضي متوسط"),
                ft.dropdown.Option("رياضي مكثف"),
            ],
        )
        result = ft.Text()

        def calc(ev):
            try:
                w = float(weight.value)
                lvl = level.value
                if lvl == "عادي":
                    g_per_kg = 1.2
                elif lvl == "رياضي متوسط":
                    g_per_kg = 1.6
                elif lvl == "رياضي مكثف":
                    g_per_kg = 2.0
                else:
                    # إذا لم يحدد المستخدم المستوى، نستخدم قيمة افتراضية
                    g_per_kg = 1.4
                protein = w * g_per_kg
                result.value = f"🍗 تحتاج إلى ~ {protein:.1f} غرام بروتين يوميًا ({g_per_kg:.2f} غ/كغ)"
            except Exception:
                result.value = "⚠️ الرجاء إدخال الوزن واختيار مستوى النشاط بشكل صحيح."
            page.update()

        page.add(
            ft.Column(
                [
                    ft.Text("🍗 حساب احتياج البروتين اليومي", size=22, weight=ft.FontWeight.BOLD),
                    weight,
                    level,
                    ft.ElevatedButton("احسب", on_click=calc),
                    result,
                    ft.TextButton("⬅️ رجوع", on_click=lambda e: home_page()),
                ],
                spacing=8,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        page.update()

    # ---------- صفحة الكربوهيدرات ----------
    def carbs_page():
        page.controls.clear()
        weight = ft.TextField(label="الوزن (كغ)", width=170)
        activity = ft.Dropdown(
            label="مستوى النشاط",
            width=170,
            options=[
                ft.dropdown.Option("خامل"),
                ft.dropdown.Option("نشاط خفيف"),
                ft.dropdown.Option("نشاط متوسط"),
                ft.dropdown.Option("نشاط عالي"),
            ],
        )
        result = ft.Text()

        def calc(ev):
            try:
                w = float(weight.value)
                act = activity.value
                # معاملات غرام كربوهيدرات لكل كغ — يمكن تعديلها حسب ما تفضّل
                factors = {"خامل": 3, "نشاط خفيف": 4, "نشاط متوسط": 5, "نشاط عالي": 6}
                g_per_kg = factors.get(act, 4)
                carbs = w * g_per_kg
                result.value = f"🍞 تحتاج إلى تقريبًا {carbs:.0f} غ كربوهيدرات يوميًا ({g_per_kg} غ/كغ)"
            except Exception:
                result.value = "⚠️ الرجاء إدخال الوزن واختيار مستوى النشاط."
            page.update()

        page.add(
            ft.Column(
                [
                    ft.Text("🍞 حساب احتياج الكربوهيدرات", size=22, weight=ft.FontWeight.BOLD),
                    ft.Row([weight, activity], spacing=10),
                    ft.ElevatedButton("احسب", on_click=calc),
                    result,
                    ft.TextButton("⬅️ رجوع", on_click=lambda e: home_page()),
                ],
                spacing=8,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        page.update()

    # ---------- صفحة الدهون ----------
    def fats_page():
        page.controls.clear()
        weight = ft.TextField(label="الوزن (كغ)", width=200)
        result = ft.Text()

        def calc(ev):
            try:
                w = float(weight.value)
                # مثال: 0.8 - 1.0 غ دهون لكل كغ — نستخدم 0.9 كقيمة افتراضية
                fats = w * 0.9
                result.value = f"🥑 تحتاج إلى تقريبًا {fats:.0f} غ دهون يوميًا"
            except Exception:
                result.value = "⚠️ الرجاء إدخال وزن صحيح."
            page.update()

        page.add(
            ft.Column(
                [
                    ft.Text("🥑 حساب احتياج الدهون اليومية", size=22, weight=ft.FontWeight.BOLD),
                    weight,
                    ft.ElevatedButton("احسب", on_click=calc),
                    result,
                    ft.TextButton("⬅️ رجوع", on_click=lambda e: home_page()),
                ],
                spacing=8,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        page.update()

    # ---------- صفحة الماء ----------
    def water_page():
        page.controls.clear()
        weight = ft.TextField(label="الوزن (كغ)", width=200)
        result = ft.Text()

        def calc(ev):
            try:
                w = float(weight.value)
                water = w * 0.033  # لتر/يوم
                result.value = f"💧 تحتاج إلى حوالي {water:.2f} لتر ماء يوميًا"
            except Exception:
                result.value = "⚠️ الرجاء إدخال وزن صحيح."
            page.update()

        page.add(
            ft.Column(
                [
                    ft.Text("💧 حساب كمية الماء اليومية", size=22, weight=ft.FontWeight.BOLD),
                    weight,
                    ft.ElevatedButton("احسب", on_click=calc),
                    result,
                    ft.TextButton("⬅️ رجوع", on_click=lambda e: home_page()),
                ],
                spacing=8,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        page.update()

    # ---------- صفحة الألياف ----------
    def fiber_page():
        page.controls.clear()
        weight = ft.TextField(label="الوزن (كغ)", width=200)
        result = ft.Text()

        def calc(ev):
            try:
                w = float(weight.value)
                fiber = w * 0.35  # غ/يوم (تقريب)
                result.value = f"🥦 تحتاج إلى حوالي {fiber:.1f} غ ألياف يوميًا"
            except Exception:
                result.value = "⚠️ الرجاء إدخال وزن صحيح."
            page.update()

        page.add(
            ft.Column(
                [
                    ft.Text("🥦 حساب الألياف اليومية", size=22, weight=ft.FontWeight.BOLD),
                    weight,
                    ft.ElevatedButton("احسب", on_click=calc),
                    result,
                    ft.TextButton("⬅️ رجوع", on_click=lambda e: home_page()),
                ],
                spacing=8,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        page.update()

    # ---------- صفحة النوم ----------
    def sleep_page():
        page.controls.clear()
        age = ft.TextField(label="العمر", width=200)
        result = ft.Text()

        def calc(ev):
            try:
                a = int(age.value)
                if a < 18:
                    sleep = "8-10 ساعات"
                elif a < 65:
                    sleep = "7-9 ساعات"
                else:
                    sleep = "7-8 ساعات"
                result.value = f"😴 يوصى بالنوم: {sleep}"
            except Exception:
                result.value = "⚠️ الرجاء إدخال عمر صحيح."
            page.update()

        page.add(
            ft.Column(
                [
                    ft.Text("😴 حساب عدد ساعات النوم المثالية", size=22, weight=ft.FontWeight.BOLD),
                    age,
                    ft.ElevatedButton("احسب", on_click=calc),
                    result,
                    ft.TextButton("⬅️ رجوع", on_click=lambda e: home_page()),
                ],
                spacing=8,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        page.update()

    # شغّل الصفحة الرئيسية أولاً
    home_page()

ft.app(target=main)
