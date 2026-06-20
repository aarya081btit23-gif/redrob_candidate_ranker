from __future__ import annotations

import tempfile
from pathlib import Path
import streamlit as st

from rank import rank_candidates, write_submission

st.set_page_config(page_title='Redrob Candidate Ranker', layout='wide')
st.title('Redrob Candidate Ranker')
st.write('Upload a `.json`, `.jsonl`, or `.jsonl.gz` candidate sample. The app returns a ranked CSV using the same offline scoring code as `rank.py`.')

uploaded = st.file_uploader('Candidate sample', type=['json', 'jsonl', 'gz'])
top_k = st.slider('Top K', 1, 100, 20)

if uploaded:
    suffix = ''.join(Path(uploaded.name).suffixes) or '.json'
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded.getvalue())
        tmp_path = tmp.name
    rows = rank_candidates(tmp_path, top_k=top_k)
    out = tempfile.NamedTemporaryFile(delete=False, suffix='.csv').name
    write_submission(rows, out)
    st.success(f'Ranked {len(rows)} candidates')
    st.dataframe([
        {
            'rank': i + 1,
            'candidate_id': r['candidate_id'],
            'score': round(r['score'], 6),
            'title': r['candidate'].get('profile', {}).get('current_title'),
            'years': r['candidate'].get('profile', {}).get('years_of_experience'),
        }
        for i, r in enumerate(rows)
    ])
    st.download_button('Download ranked CSV', data=Path(out).read_bytes(), file_name='ranked_candidates.csv', mime='text/csv')
