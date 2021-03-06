
import os
import sys
import platform
import pickle
from pandas import read_pickle

from .dataFieldNames import *


def loadFiles(pbp_file='DataDumps/NBA/pbpSubset02.pkl',
              moments_file='DataDumps/NBA/momentsSubset02.pkl'):
    # [u'0041400161', u'0041400163', u'0041400164', u'0021400648']

    if 'trusty' in platform.platform():
        base = '/media/immersinn/dataDumps' 
    elif 'wily' in platform.platform():
        base = '/home/immersinn/Data'

    pbp_file = os.path.join(base, pbp_file)
    moments_file = os.path.join(base, moments_file)

##    with open('/home/immersinn/Data/DataDumps/NBA/momentsSubset02.pkl', 'rb') as f1:
##        moments = pickle.Unpickler(f1).load()
##               
##    with open('/home/immersinn/Data/DataDumps/NBA/pbpSubset02.pkl', 'rb') as f1:
##        pbp = pickle.Unpickler(f1).load()

    pbp = read_pickle(pbp_file)
    moments = read_pickle(moments_file)

    return(moments, pbp)


def grabGameFromLoad(gid = '0041400161'):
    """

    returns:
        moments : list of dicts
        pbp : pbp DataFrame
    """
    # Load data
    mom_list, pbp_list = loadFiles()

    # Preprocess
    ## None...pass raw out..


    # Retrieve data for specified game
    moments = [m for m in mom_list if m['game_id'] == gid]
    pbp = [p for p in pbp_list if p['game_id'] == gid] 

    return(moments, pbp)


def main():

    moments, pbp = loadFiles()
    gids = set([g for (g, _, _) in moments])
    mom_dict = {}
    for gid in gids:
        mom_dict[gid] = [(g, e, d) for (g, e, d) in moments if g == gid]
    pbp_dict = {}
    for p in pbp:
        pbp_dict[p['game_id']] = p['play_by_play']

    return(pbp_dict, mom_dict)
