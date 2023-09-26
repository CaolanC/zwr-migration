import json
import srcomapi, srcomapi.datatypes as dt
api = srcomapi.SpeedrunCom(); api.debug = 1

game_name = "Call of Duty: Black Ops III Zombies"

path = '../download/zwr.gg/leaderboards/bo3/ee-speedrun/shadows-of-evil/bo3-shadows-of-evil-ee-speedrun-all-gobblegum-1-board.json'

def singleRun(game_n):

    for data in parse():

        print(data)
        end_run = {"run": {"comment":"Submitted during migration from zwr by honch"}}

        game = api.search(srcomapi.datatypes.Game, {"name":game_n})
        game = game[0].categories[0]

        end_run["run"]["category"] = game.id
        #end_run["times"] = {"ingame":data[0]}
        end_run["video"] = data[1]
        print(end_run)        

def parse():

    f = open(path)
    data = json.load(f)
    f.close()

    data_t = []

    for i in range(1, 300):
        if str(i) in data:
            run = data[str(i)][0]
            mins_seconds = [int(i) for i in run['achieved'].split(":")]
            ingame_time = mins_seconds[0] * 60 + mins_seconds[1]
            video = run['main_video']
            data_t.append([ingame_time, video])

        else:

            break

    print(f'{i} runs found')
    return data_t

print(singleRun(game_name))
#]parse()
