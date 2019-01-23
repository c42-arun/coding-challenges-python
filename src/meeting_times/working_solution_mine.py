def merge_ranges(meetings):
    # sort the meetings by start time
    # - sorting a list of tuples by default sorts by first element
    # - https://algocoding.wordpress.com/2015/04/14/how-to-sort-a-list-of-tuples-in-python-3-4/
    meetings.sort()

    merged_meetings = []
    # initialise with first meeting
    current_meet = meetings[0]

    for meet in meetings:
        # if start time is later than current meeting's end time then this is a new slot.
        # add current meeting to meeting list and start a new meeting slot with this meet
        if (meet[0] > current_meet[1]):
            merged_meetings.append(current_meet)
            current_meet = meet
        else:
            # if meeting's end time is later than current meeting's end time then
            # extend current meeting end time to this meeting's end time (merge in other words)
            if (meet[1] > current_meet[1]):
                current_meet = (current_meet[0], meet[1])
    
    merged_meetings.append(current_meet) # add the last running meeting to the list

    return merged_meetings

if __name__ == "__main__":
    # meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    
    ## These meetings should probably be merged, although they don't exactly "overlap"—they just "touch." Does your function do this?
    # meetings = [(1, 2), (2, 3)]

    ## Notice that although the second meeting starts later, it ends before the first meeting ends. 
    ## Does your function correctly handle the case where a later meeting is "subsumed by" an earlier meeting?
    # meetings =   [(1, 5), (2, 3)]

    ## Here all of our meetings should be merged together into just (1, 10). 
    ## We need keep in mind that after we've merged the first two we're not done with the result — 
    ##  the result of that merge may itself need to be merged into other meetings as well.
    # meetings = [(1, 10), (2, 6), (3, 5), (7, 9)]

    ## Make sure that your function won't "leave out" the last meeting.
    # meetings = [(1, 10), (2, 6), (3, 5), (17, 19)]
    merged_meetings = merge_ranges(meetings)

    ## We can do this in O(n\lg{n})O(nlgn) time.
    # Yes as we sorted in the first time - O(n lg n), then O(n) for single loop pass, so O(n lg n) in total
    print(merged_meetings)