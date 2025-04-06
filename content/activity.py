import streamlit as st
import pandas as pd

def display_activities():
    st.header("Activities Schedule")

    # Store activities data in lists
    activities = [
        "Boys Halaqa",
        "Quran Halaqa (Men)",
        "Arabic Class (4-5 y)",
        "Girls Halaqa (16+ y)",
        "Arabic Class (7-9 y)",
        "Sisters Halaqa"
    ]

    days = [
        "Saturday & Sunday",
        "Saturday & Sunday",
        "Tuesday & Friday",
        "Saturday",
        "Wednesday & Friday",
        "Thursday"
    ]

    times = [
        "2:00pm-5:00pm",
        "5:30pm-9:00pm",
        "3:30pm-5:00pm",
        "6:00pm-8:00pm",
        "3:30pm-5:00pm",
        "10:00am-12:00pm"
    ]

    # Create DataFrame
    df = pd.DataFrame({
        "Activity": activities,
        "Day": days,
        "Time": times
    })

    # Display the table with Streamlit
    st.dataframe(
        df,
        hide_index=True,
        use_container_width=True,  # Make table use full container width
        column_config={
            "Activity": st.column_config.TextColumn(
                "Activity",
                width=None,
            ),
            "Day": st.column_config.TextColumn(
                "Day",
                width=None,
            ),
            "Time": st.column_config.TextColumn(
                "Time",
                width=None,
            ),
        }
    )

if __name__ == "__main__":
    display_activities() 