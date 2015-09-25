import pybossa.cache.project_stats as project_stats
import pybossa.stats_contribua as stats_contribua
from flask.ext.plugins import Plugin
from functools import wraps


__plugin__ = "EngagementStats"
__version__ = "0.0.1"



def update_stats(f):
    @wraps(f)
    def wrapper(project_id, geo=False, period='2 week'):
        project_update = f(project_id) #tuple
        project_update[2]['users'].update(stats_contribua.get_engagement_stats())
        return project_update
    return wrapper
 

class EngagementStats(Plugin):

    def setup(self):
    	project_stats.get_stats = update_stats(project_stats.get_stats)        
