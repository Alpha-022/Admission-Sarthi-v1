def finalList(rank1, perc, category, university, gender, pwd, sortby, branch):
    import pandas as pd
    from pathlib import Path

    # Read the dataset
    base_path = Path(__file__).parent
    file_path = (base_path / "..//app//round1_cleaned.csv").resolve()
    df = pd.read_csv(file_path)

    # Convert rank to float if provided as a string
    rank = float(rank1) if rank1 != '-1' else None

    # Filter based on category, gender, PwD status, and rank
    if pwd == 'YES':
        catg = category + '-PwD'
        p = df[(df['Rank'] >= rank) & ((df['Category'] == catg) | (df['Category'] == 'OPEN-PwD'))]
    else:
        p = df[(df['Rank'] >= rank) & ((df['Category'] == category) | (df['Category'] == 'OPEN'))]

    # Filter based on university and quota
    v = p[((p['University'] == university) | (p['University'] == 'All India')) & (p['Quota'] != 'HU')].index
    q = p.drop(index=v)

    # Filter based on branch (if provided)
    if branch:
        q = q[q['Branch Name'].str.strip() == branch.strip()]

    # Calculate probability of admission based on user's percentile and actual cutoff percentile
    # q['Probability'] = 100 * (q['Percentile'] / perc)
    if perc:
        q['Probability'] = 100 * (perc / q['Percentile'])
    elif rank:
        q['Probability'] = 100 * (rank / q['Rank'])


    # Ensure probabilities are capped at 100%
    q['Probability'] = q['Probability'].clip(upper=100)
    
    # Sort the filtered data by Percentile in descending order
    q = q.sort_values(by='Percentile', ascending=False)

    # Drop unnecessary columns and duplicates
    x = q.drop(['Quota', 'Seat Pool', 'University', 'Round No'], axis=1).drop_duplicates()

    # Reset index and return filtered data
    x.reset_index(inplace=True, drop=True)
    return x

