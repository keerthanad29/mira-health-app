import streamlit as st
import re
from datetime import date
from database import create_table, create_patient, get_all_patients, get_patient_by_id, update_patient, delete_patient
from ai_service import get_health_prediction

# Page config
st.set_page_config(
    page_title="MIRA - Medical Intelligence",
    page_icon="🏥",
    layout="wide"
)

# Initialize database
create_table()

# Title
st.title("🏥 MIRA - Medical Intelligence Robotic Automation")
st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["➕ Add Patient", "📋 View Patients", "✏️ Update Patient", "🗑️ Delete Patient"])

# ─────────────────────────────────────────
# TAB 1: ADD PATIENT
# ─────────────────────────────────────────
with tab1:
    st.header("Add New Patient")

    col1, col2 = st.columns(2)

    with col1:
        full_name = st.text_input("Full Name")
        dob = st.date_input("Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())
        email = st.text_input("Email Address")

    with col2:
        glucose = st.number_input("Glucose (mg/dL)", min_value=0.0, max_value=999.0, step=0.1)
        haemoglobin = st.number_input("Haemoglobin (g/dL)", min_value=0.0, max_value=99.0, step=0.1)
        cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=0.0, max_value=999.0, step=0.1)

    if st.button("🔍 Predict & Save", use_container_width=True):
        errors = []

        if not full_name.strip():
            errors.append("Full Name is required.")

        if not email.strip():
            errors.append("Email is required.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Invalid email format.")

        if dob >= date.today():
            errors.append("Date of Birth cannot be today or a future date.")

        if glucose <= 0:
            errors.append("Glucose must be greater than 0.")

        if haemoglobin <= 0:
            errors.append("Haemoglobin must be greater than 0.")

        if cholesterol <= 0:
            errors.append("Cholesterol must be greater than 0.")

        if errors:
            for error in errors:
                st.error(error)
        else:
            with st.spinner("🤖 AI Analyzing blood test results..."):
                remarks = get_health_prediction(
                    full_name, str(dob), glucose, haemoglobin, cholesterol
                )

            create_patient(full_name, str(dob), email, glucose, haemoglobin, cholesterol, remarks)
            st.success(f"✅ Patient '{full_name}' added successfully!")
            st.info(f"🤖 AI Remarks: {remarks}")

# ─────────────────────────────────────────
# TAB 2: VIEW PATIENTS
# ─────────────────────────────────────────
with tab2:
    st.header("All Patients")

    patients = get_all_patients()

    if not patients:
        st.warning("No patients found. Add a patient first!")
    else:
        import pandas as pd
        df = pd.DataFrame(patients, columns=["ID", "Full Name", "DOB", "Email", "Glucose", "Haemoglobin", "Cholesterol", "Remarks"])
        st.dataframe(df, use_container_width=True)
        st.success(f"Total Patients: {len(patients)}")

# ─────────────────────────────────────────
# TAB 3: UPDATE PATIENT
# ─────────────────────────────────────────
with tab3:
    st.header("Update Patient Record")

    patients = get_all_patients()

    if not patients:
        st.warning("No patients found. Add a patient first!")
    else:
        patient_ids = {f"{p[1]} (ID: {p[0]})": p[0] for p in patients}
        selected = st.selectbox("Select Patient to Update", list(patient_ids.keys()))
        patient_id = patient_ids[selected]
        patient = get_patient_by_id(patient_id)

        col1, col2 = st.columns(2)

        with col1:
            new_name = st.text_input("Full Name", value=patient[1])
            new_dob = st.date_input("Date of Birth",
                                     value=date.fromisoformat(patient[2]),
                                     min_value=date(1900, 1, 1),
                                     max_value=date.today())
            new_email = st.text_input("Email Address", value=patient[3])

        with col2:
            new_glucose = st.number_input("Glucose (mg/dL)", min_value=0.0, max_value=999.0, value=float(patient[4]), step=0.1)
            new_haemoglobin = st.number_input("Haemoglobin (g/dL)", min_value=0.0, max_value=99.0, value=float(patient[5]), step=0.1)
            new_cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=0.0, max_value=999.0, value=float(patient[6]), step=0.1)

        if st.button("🔄 Re-Predict & Update", use_container_width=True):
            errors = []

            if not new_name.strip():
                errors.append("Full Name is required.")

            if not new_email.strip():
                errors.append("Email is required.")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
                errors.append("Invalid email format.")

            if new_dob >= date.today():
                errors.append("Date of Birth cannot be today or a future date.")

            if new_glucose <= 0:
                errors.append("Glucose must be greater than 0.")

            if new_haemoglobin <= 0:
                errors.append("Haemoglobin must be greater than 0.")

            if new_cholesterol <= 0:
                errors.append("Cholesterol must be greater than 0.")

            if errors:
                for error in errors:
                    st.error(error)
            else:
                with st.spinner("🤖 AI Re-Analyzing..."):
                    new_remarks = get_health_prediction(
                        new_name, str(new_dob), new_glucose, new_haemoglobin, new_cholesterol
                    )

                update_patient(patient_id, new_name, str(new_dob), new_email, new_glucose, new_haemoglobin, new_cholesterol, new_remarks)
                st.success(f"✅ Patient '{new_name}' updated successfully!")
                st.info(f"🤖 New AI Remarks: {new_remarks}")

# ─────────────────────────────────────────
# TAB 4: DELETE PATIENT
# ─────────────────────────────────────────
with tab4:
    st.header("Delete Patient Record")

    patients = get_all_patients()

    if not patients:
        st.warning("No patients found. Add a patient first!")
    else:
        patient_ids = {f"{p[1]} (ID: {p[0]})": p[0] for p in patients}
        selected = st.selectbox("Select Patient to Delete", list(patient_ids.keys()))
        patient_id = patient_ids[selected]
        patient = get_patient_by_id(patient_id)

        st.write("**Patient Details:**")
        st.write(f"- Name: {patient[1]}")
        st.write(f"- DOB: {patient[2]}")
        st.write(f"- Email: {patient[3]}")

        st.warning("⚠️ This action cannot be undone!")

        if st.button("🗑️ Delete Patient", use_container_width=True):
            delete_patient(patient_id)
            st.success(f"✅ Patient '{patient[1]}' deleted successfully!")
            st.rerun()