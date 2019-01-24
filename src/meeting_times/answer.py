def merge_ranges(meetings):
    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        
        # deconstruct the tuple elements
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings

if __name__ == "__main__":
    meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    
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