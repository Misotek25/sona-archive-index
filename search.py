import argparse

def keyword_search(speeches, keyword):
    return [speech for speech in speeches if keyword.lower() in speech['text'].lower()]

def speaker_search(speeches, speaker):
    return [speech for speech in speeches if speech['speaker'].lower() == speaker.lower()]

def year_based_filter(speeches, year):
    return [speech for speech in speeches if speech['year'] == year]

def interactive_search(speeches):
    while True:
        keyword = input("Enter keyword (or 'exit' to quit): ")
        if keyword.lower() == 'exit':
            break
        results = keyword_search(speeches, keyword)
        display_results(results)

def display_results(results):
    for r in results:
        print(f"{r['year']} - {r['speaker']}: {r['text'][:50]}...")  # Show first 50 characters

def main():
    parser = argparse.ArgumentParser(description='Search SONA speeches.')
    parser.add_argument('--keyword', type=str, help='Search by keyword')
    parser.add_argument('--speaker', type=str, help='Search by speaker')
    parser.add_argument('--year', type=int, help='Filter by year')
    args = parser.parse_args()

    # Example speeches data structure for illustration
    speeches = [
        {'year': 2021, 'speaker': 'Speaker A', 'text': 'This is a speech about economy.'},
        {'year': 2022, 'speaker': 'Speaker B', 'text': 'This is a speech about education.'},
        # More speeches...
    ]

    if args.keyword:
        results = keyword_search(speeches, args.keyword)
        display_results(results)
    elif args.speaker:
        results = speaker_search(speeches, args.speaker)
        display_results(results)
    elif args.year:
        results = year_based_filter(speeches, args.year)
        display_results(results)
    else:
        print("Starting interactive search...")
        interactive_search(speeches)

if __name__ == "__main__":
    main()