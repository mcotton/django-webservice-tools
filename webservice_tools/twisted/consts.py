# -*- coding: utf-8 -*-
###
#MISC
PERIOD_SLEEP_ON_FATAL_ERROR = 2
MAX_EMAILED_EXCEPTIONS_PER_RUN = 30
COMMON_SUGGESTED_THREADPOOL_SIZE = 30

MEMCACHED_DEFAULT_EXPIRE_PERIOD = 60 #in seconds
MEMCACHED_SHORT_EXPIRE_PERIOD = 30 #in seconds
MEMCACHED_SHORTER_EXPIRE_PERIOD = 15 #in seconds
MEMCACHED_VERY_SHORT_EXPIRE_PERIOD = 5 #in seconds
MEMCACHED_NO_EXPIRE_PERIOD = 0 #in seconds
MEMCACHED_LONG_EXPIRE_PERIOD = 320 #in seconds
MEMCACHED_EXPIRE_PERIOD_1H = 3600 #in seconds
MEMCACHED_EXPIRE_PERIOD_1D = 86400 #in seconds
MEMCACHED_EXPIRE_PERIOD_1W = 604800 #in seconds
MISC_MEMCACHED_PORT = 11211 #if changed, should also be changed in memcached.conf
IBL_API_MEMCACHE_DEFAULT_LIFETIME = 380 #in seconds

DBUTIL_PB_CLIENT_PING_INTERVAL = 30 #in seconds

LOGLVL_DEBUG2 = 9
LOGLVL_DEBUG3 = 8
LOGLVL_ALWAYS = 100

#############################
#MODULE FUNCTIONALITY
#############################