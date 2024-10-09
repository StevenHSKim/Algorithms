def times_to_seconds(times):
    minutes = int(times[:2])
    seconds = int(times[3:])
    return minutes * 60 + seconds

def seconds_to_times(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f'{minutes:02}:{seconds:02}'

def solution(video_len, pos, op_start, op_end, commands):
    video_len = times_to_seconds(video_len)
    pos = times_to_seconds(pos)
    op_start = times_to_seconds(op_start)
    op_end = times_to_seconds(op_end)
    
    if op_start <= pos <= op_end:
        pos = op_end
    
    for c in commands:
        if c == "next":
            pos = min(pos+10, video_len)
        if c == "prev":
            pos = max(0, pos-10)
    
        if op_start <= pos <= op_end:
            pos = op_end
        
    return seconds_to_times(pos)