{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "51e4e7f3-2ad8-4648-8943-8b17600078b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: streamlit in /usr/local/lib/python3.10/site-packages (1.28.2)\n",
      "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/site-packages (from streamlit) (4.2.0)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/local/lib/python3.10/site-packages (from streamlit) (1.4)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/site-packages (from streamlit) (5.3.1)\n",
      "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/site-packages (from streamlit) (8.1.3)\n",
      "Requirement already satisfied: importlib-metadata<7,>=1.4 in /usr/local/lib/python3.10/site-packages (from streamlit) (4.12.0)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in /usr/local/lib/python3.10/site-packages (from streamlit) (1.23.5)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in /usr/local/lib/python3.10/site-packages (from streamlit) (22.0)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in /usr/local/lib/python3.10/site-packages (from streamlit) (1.5.3)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in /usr/local/lib/python3.10/site-packages (from streamlit) (9.1.1)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in /usr/local/lib/python3.10/site-packages (from streamlit) (3.20.3)\n",
      "Requirement already satisfied: pyarrow>=6.0 in /usr/local/lib/python3.10/site-packages (from streamlit) (8.0.0)\n",
      "Requirement already satisfied: python-dateutil<3,>=2.7.3 in /usr/local/lib/python3.10/site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/site-packages (from streamlit) (2.28.1)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/site-packages (from streamlit) (13.5.3)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in /usr/local/lib/python3.10/site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/site-packages (from streamlit) (4.5.0)\n",
      "Requirement already satisfied: tzlocal<6,>=1.1 in /usr/local/lib/python3.10/site-packages (from streamlit) (5.2)\n",
      "Requirement already satisfied: validators<1,>=0.2 in /usr/local/lib/python3.10/site-packages (from streamlit) (0.22.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.10/site-packages (from streamlit) (3.1.27)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.10/site-packages (from streamlit) (0.8.1b0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/site-packages (from streamlit) (6.2)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in /usr/local/lib/python3.10/site-packages (from streamlit) (2.1.9)\n",
      "Requirement already satisfied: entrypoints in /usr/local/lib/python3.10/site-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
      "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/site-packages (from altair<6,>=4.0->streamlit) (3.1.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/site-packages (from altair<6,>=4.0->streamlit) (4.17.3)\n",
      "Requirement already satisfied: toolz in /usr/local/lib/python3.10/site-packages (from altair<6,>=4.0->streamlit) (0.11.2)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.10/site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.9)\n",
      "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.10/site-packages (from importlib-metadata<7,>=1.4->streamlit) (3.8.0)\n",
      "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/site-packages (from pandas<3,>=1.3.0->streamlit) (2022.1)\n",
      "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/site-packages (from python-dateutil<3,>=2.7.3->streamlit) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer<3,>=2 in /usr/local/lib/python3.10/site-packages (from requests<3,>=2.27->streamlit) (2.1.0)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/site-packages (from requests<3,>=2.27->streamlit) (3.3)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/site-packages (from requests<3,>=2.27->streamlit) (1.26.9)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/site-packages (from requests<3,>=2.27->streamlit) (2022.6.15)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/site-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/site-packages (from rich<14,>=10.14.0->streamlit) (2.16.1)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.10/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.1)\n",
      "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.10/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.1)\n",
      "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "b460e38e-f798-40e7-a0ec-19924176c4b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: pandas in /usr/local/lib/python3.10/site-packages (1.5.3)\n",
      "Requirement already satisfied: numpy in /usr/local/lib/python3.10/site-packages (1.23.5)\n",
      "Requirement already satisfied: nltk in /usr/local/lib/python3.10/site-packages (3.8.1)\n",
      "Requirement already satisfied: textblob in /usr/local/lib/python3.10/site-packages (0.17.1)\n",
      "Requirement already satisfied: matplotlib in /usr/local/lib/python3.10/site-packages (3.6.3)\n",
      "Requirement already satisfied: seaborn in /usr/local/lib/python3.10/site-packages (0.12.2)\n",
      "Requirement already satisfied: wordcloud in /usr/local/lib/python3.10/site-packages (1.9.2)\n",
      "Requirement already satisfied: python-dateutil>=2.8.1 in /usr/local/lib/python3.10/site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/site-packages (from pandas) (2022.1)\n",
      "Requirement already satisfied: click in /usr/local/lib/python3.10/site-packages (from nltk) (8.1.3)\n",
      "Requirement already satisfied: joblib in /usr/local/lib/python3.10/site-packages (from nltk) (1.2.0)\n",
      "Requirement already satisfied: regex>=2021.8.3 in /usr/local/lib/python3.10/site-packages (from nltk) (2022.6.2)\n",
      "Requirement already satisfied: tqdm in /usr/local/lib/python3.10/site-packages (from nltk) (4.64.0)\n",
      "Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.10/site-packages (from matplotlib) (1.0.7)\n",
      "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.10/site-packages (from matplotlib) (0.11.0)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.10/site-packages (from matplotlib) (4.33.3)\n",
      "Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.10/site-packages (from matplotlib) (1.4.3)\n",
      "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/site-packages (from matplotlib) (22.0)\n",
      "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.10/site-packages (from matplotlib) (9.1.1)\n",
      "Requirement already satisfied: pyparsing>=2.2.1 in /usr/local/lib/python3.10/site-packages (from matplotlib) (3.0.9)\n",
      "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/site-packages (from python-dateutil>=2.8.1->pandas) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pandas numpy nltk textblob matplotlib seaborn wordcloud"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "29f6790d-5dcb-469a-a11d-d5e8a1bbd6c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "from wordcloud import WordCloud\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a101ef6f-4d4f-41af-9bce-9bb809faa73c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load the data\n",
    "file_path = 'job_descriptions.csv'  # Update with the correct file path\n",
    "data = pd.read_csv(file_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "145904af-902a-444c-bf33-140f43f5cb1e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Streamlit App\n",
    "st.set_page_config(page_title=\"Job Insights Dashboard\", layout=\"wide\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "058ef92f-90b9-4a65-85ba-9e93716222d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-12-05 10:29:32.059 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /usr/local/lib/python3.10/site-packages/ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "# Sidebar - Filters\n",
    "st.sidebar.header(\"Filters\")\n",
    "job_title_filter = st.sidebar.selectbox(\"Select Job Title\", [\"All\"] + list(data[\"Job_Title\"].unique()))\n",
    "experience_filter = st.sidebar.selectbox(\"Select Experience Level\", [\"All\"] + list(data[\"Experience_Level\"].unique()))\n",
    "location_filter = st.sidebar.selectbox(\"Select Location\", [\"All\"] + list(data[\"Location\"].unique()))\n",
    "industry_filter = st.sidebar.selectbox(\"Select Industry\", [\"All\"] + list(data[\"Industry\"].unique()))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a27dd1d7-b365-440a-8bc1-342f2bac16bc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Apply Filters\n",
    "filtered_data = data.copy()\n",
    "if job_title_filter != \"All\":\n",
    "    filtered_data = filtered_data[filtered_data[\"Job_Title\"] == job_title_filter]\n",
    "if experience_filter != \"All\":\n",
    "    filtered_data = filtered_data[filtered_data[\"Experience_Level\"] == experience_filter]\n",
    "if location_filter != \"All\":\n",
    "    filtered_data = filtered_data[filtered_data[\"Location\"] == location_filter]\n",
    "if industry_filter != \"All\":\n",
    "    filtered_data = filtered_data[filtered_data[\"Industry\"] == industry_filter]\n",
    "\n",
    "# Main Page\n",
    "st.title(\"Job Insights Dashboard\")\n",
    "st.markdown(\"Use the filters on the left to customize your insights.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5dfb52c7-550f-4c55-97eb-a9e869f0550d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Visualization 1: Salary Range Distribution\n",
    "st.subheader(\"Salary Range Distribution\")\n",
    "salary_dist = sns.countplot(data=filtered_data, x=\"Salary_Range\", order=data[\"Salary_Range\"].value_counts().index, palette=\"muted\")\n",
    "st.pyplot(salary_dist.figure)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "e27fa412-52b5-463f-98a9-70a4a088d745",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Visualization 2: Experience Level Breakdown\n",
    "st.subheader(\"Experience Level Breakdown\")\n",
    "exp_level_dist = sns.countplot(data=filtered_data, x=\"Experience_Level\", order=data[\"Experience_Level\"].value_counts().index, palette=\"pastel\")\n",
    "st.pyplot(exp_level_dist.figure)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "972d6672-a9d4-43f7-b8c5-c37e5e3e8191",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Tooltips\n",
    "with st.expander(\"How to Use This Dashboard\"):\n",
    "    st.write(\"\"\"\n",
    "    - **Filters**: Use the sidebar to filter the data by job title, experience level, location, and industry.\n",
    "    - **Salary Range Distribution**: View the distribution of jobs across different salary ranges.\n",
    "    - **Experience Level Breakdown**: Analyze the proportion of jobs based on experience level.\n",
    "    - **Word Cloud**: See the most frequently required skills for the filtered jobs.\n",
    "    \"\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9944c91a-a086-4a93-8cb7-0bd8423cf1d1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 [3.10]",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
