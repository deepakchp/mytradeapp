import pandas as pd
def get_position(data,st_signal):
    position = []
    for i in range(len(st_signal)):
        #position.append(0)
        if st_signal[i] > 1:
            position.append(0)
        else:
            position.append(1)
        
    for i in range(len(data['close'])):
        if st_signal[i] == 1:
            position[i] = 1
        elif st_signal[i] == -1:
            position[i] = 0
        else:
            position[i] = position[i-1]
        
    close_price = data['close']
    st = data['st']
    st_signal = pd.DataFrame(st_signal).rename(columns = {0:'st_signal'}).set_index(data.index)
    position = pd.DataFrame(position).rename(columns = {0:'st_position'}).set_index(data.index)

    frames = [close_price, st, st_signal, position]
    strategy = pd.concat(frames, join = 'inner', axis = 1)
    
    return strategy