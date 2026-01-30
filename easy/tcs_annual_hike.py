def calculate_annual_hike(current_ctc: int, hikes: list):
    new_ctc = list()
    for hike in hikes:
        ctc = current_ctc + (current_ctc * (hike/100))
        new_ctc.append(ctc)

    return new_ctc


if __name__ == '__main__':
    print("=====Calculating Possible New CTC after Hike=====")
    current_ctc = 525000
    hikes = [8,5]
    result:list = calculate_annual_hike(current_ctc, hikes)
    i = 0
    for res in result:
        print(f"New CTC will be {res} for {hikes[i]} % hike. So In-hand salary will be around ",res/14.85)
        i = i + 1