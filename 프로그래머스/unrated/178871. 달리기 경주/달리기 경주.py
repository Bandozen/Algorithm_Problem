def solution(players, callings):
    player_num = {player : i for i, player in enumerate(players)}
    num_player = {i : player for i, player in enumerate(players)}
    
    for i in callings:
        current_num = player_num[i]
        pre_num = current_num - 1

        current_player = i
        pre_player = num_player[pre_num]
        
        player_num[current_player] = pre_num
        player_num[pre_player] = current_num
        
        num_player[pre_num] = current_player
        num_player[current_num] = pre_player

    return list(num_player.values())