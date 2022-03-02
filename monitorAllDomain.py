from datetime import datetime, timedelta

import wlstModule as wlst
import sys
import traceback

import thread
import time


def vToSTR(VARTOSTR):
	VARTOSTR = str(VARTOSTR).replace(",", "|")
	return VARTOSTR
	
def vNoTIM():
	now = datetime.now()
	VARGTIME = now.strftime("%d/%m/%Y %H:%M:%S")
	return VARGTIME

def domainConnect(CONFIG,KEY,ADM,WLURL):
	print '<+> ---------------------------------------------------------------------------------------------- <+>'; print;
	try:
		connect(userConfigFile=CONFIG, userKeyFile=KEY, url=WLURL)
		import thread
		import time

		allServers=domainRuntimeService.getServerRuntimes();
		if (len(allServers) > 0):
			print('%-20s %-20s %-20s' % ('HEALTH:','SERVER:','STATE:'));
			for tempServer in allServers:
				serverhealth = tempServer.getOverallHealthState()
				if (tempServer.getState() != "RUNNING") or not ("HEALTH_OK" in str(serverhealth)):
					print 'MN Server Name         '  ,  tempServer.getName();
					print 'MN Server State        '  ,  tempServer.getState();
					print 'MN Server Health State '  ,  tempServer.getOverallHealthState();
					print('%-20s %-20s %-20s' % ('ERROR',tempServer.getName(),'ERROR_STATUS'));
				else:
					print('%-20s %-20s %-20s' % ('OK',tempServer.getName(),tempServer.getState()));
		print;
		getDataSources()
		getDataJMS()
		getAppDeploys()
	except:
		print 'ERROR_DOMAIN_CONNECT';
		writeToFile("monitorPRD.ERROR.DOMAIN.CONNECT",0,CONFIG,KEY,ADM+',['+WLURL+'],'+vNoTIM())
	print '<+> ------------------------------------ <+>'

domainRuntime()

def checkHealth(serverName):
    slrBean = cmo.lookupServerLifeCycleRuntime(serverName)
    status = slrBean.getState()
    import thread
    import time
	
    if not ("RUNNING" in str(status)):
        print '(IfNot) ACTUAL STATUS [ '+serverName+' ]'
        state(serverName,'Server')

    try:
      # print 
      cd("/ServerRuntimes/"+serverName+"/JVMRuntime/"+serverName);    ##ls()
      varGetHeapCurr = int(cmo.getHeapSizeCurrent())/(1024*1024);     ## writeToFile("monitorPRD__HEAP_Current"                       ,0,domainName,serverName,varGetHeapCurr)
      varGetHeapFree = int(cmo.getHeapFreeCurrent())/(1024*1024);     ## writeToFile("monitorPRD__HEAP_FreeMem"                       ,0,domainName,serverName,varGetHeapFree)
      varGetHeapMaxm = int(cmo.getHeapSizeMax())/(1024*1024);         ## writeToFile("monitorPRD__HEAP_Maximum"                       ,0,domainName,serverName,varGetHeapMaxm)
      varGetHeapTota = str(get('TotalHeap')/(1024*1024));             ## writeToFile("monitorPRD__HEAP_TotalHP"                       ,0,domainName,serverName,varGetHeapTota)
      varGetHeapUsed = str(get('UsedHeap')/(1024*1024));              ## writeToFile("monitorPRD__HEAP_UsedHea"                       ,0,domainName,serverName,varGetHeapUsed)
      varGetHeapFPct = int(cmo.getHeapFreePercent());                 ## writeToFile("monitorPRD__HEAP_PerFree"                       ,0,domainName,serverName,varGetHeapFPct)
      varGetHeapUPct = int(100-varGetHeapFPct);                       ## writeToFile("monitorPRD__HEAP_PerUsed"                       ,0,domainName,serverName,varGetHeapUPct)
      varGetServStat = status;                                        ## writeToFile("monitorPRD__STAT_StateMS"                       ,0,domainName,serverName,varGetServStat)
      #------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
      tmpGetTimeSecU = timedelta(seconds=int(cmo.getUptime())/1000)
      tmpGetTimeDayU = datetime(1,1,1) + tmpGetTimeSecU               ## print("[%d Dias][%d Horas]       : " % (tmpGetTimeDayU.day-1, tmpGetTimeDayU.hour))
      varGetTimeDayD = (tmpGetTimeDayU.day-1);                        ## writeToFile("monitorPRD__TIME_TDaysUP"                       ,0,domainName,serverName,varGetTimeDayD)
	  #------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
      varGetPER_0000 = str(get('JvmProcessorLoad')*100);                  writeToFile("monitorPRD_PER_JVM_JvmProcessorLoad"            ,0,domainName,serverName,varGetPER_0000)
      varGetPER_0001 = str(get('AllProcessorsAverageLoad')*100);          writeToFile("monitorPRD_PER_CPU_AllProcessorsAverageLoad"    ,0,domainName,serverName,varGetPER_0001)
      varGetPER_0002 = str(get('NumberOfDaemonThreads'));                 writeToFile("monitorPRD_PER_CPU_NumberOfDaemonThreads"       ,0,domainName,serverName,varGetPER_0002)
      varGetPER_0003 = str(get('NumberOfProcessors'));                    writeToFile("monitorPRD_PER_CPU_NumberOfProcessors"          ,0,domainName,serverName,varGetPER_0003)
      varGetPER_0004 = str(get('TotalGarbageCollectionCount'));           writeToFile("monitorPRD_PER_GCJ_TotalGarbageCollectionCount" ,0,domainName,serverName,varGetPER_0004)
      varGetPER_0005 = str(get('TotalGarbageCollectionTime')/1000);       writeToFile("monitorPRD_PER_GCJ_TotalGarbageCollectionTime"  ,0,domainName,serverName,varGetPER_0005)
      varGetPER_0006 = str(get('TotalNumberOfThreads'));                  writeToFile("monitorPRD_PER_CPU_TotalNumberOfThreads"        ,0,domainName,serverName,varGetPER_0006)
      varGetPER_0007 = str(get('TotalNurserySize')/(1024*1024));          writeToFile("monitorPRD_PER_MEM_TotalNurserySize"            ,0,domainName,serverName,varGetPER_0007)
      varGetPER_0008 = str(get('TotalPhysicalMemory')/(1024*1024));       writeToFile("monitorPRD_PER_MEM_TotalPhysicalMemory"         ,0,domainName,serverName,varGetPER_0008)
      varGetPER_0009 = str(get('UsedPhysicalMemory')/(1024*1024));        writeToFile("monitorPRD_PER_MEM_UsedPhysicalMemory"          ,0,domainName,serverName,varGetPER_0009)
      #------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
      cd('/ServerRuntimes/'+serverName); #ls()
      varGetSeHealtR = str(get('HealthState'));
      if ("HEALTH_OK" in str(varGetSeHealtR)): varGetSeHealtR = 'HEALTH_OK';
      else: varGetSeHealtR = 'HEALTH_ERROR'
      # writeToFile("monitorPRD__STAT_HealthRun",0,domainName,serverName,varGetSeHealtR)
      
      varGetSeHealtA = str(cmo.getOverallHealthState());
      if ("HEALTH_OK" in str(varGetSeHealtA)): varGetSeHealtA = 'HEALTH_OK';
      else: varGetSeHealtA = 'HEALTH_ERROR'
      # writeToFile("monitorPRD__STAT_HealthApp",0,domainName,serverName,varGetSeHealtA)
      
      varGetSockOpnC = String.valueOf(cmo.getOpenSocketsCurrentCount());  writeToFile("monitorPRD_PER_SOCKET_OpenCurrentCount"         ,0,domainName,serverName,varGetSockOpnC)
      varGetSockOTot = String.valueOf(cmo.getSocketsOpenedTotalCount());  writeToFile("monitorPRD_PER_SOCKET_OpenedTotalCount"         ,0,domainName,serverName,varGetSockOTot)
      #------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
      cd('/ServerRuntimes/'+serverName+'/ThreadPoolRuntime/ThreadPoolRuntime'); #ls()
      varGetReqCompl = str(cmo.getCompletedRequestCount());               writeToFile("monitorPRD_PER_REQUEST_CompletedRequestCount"   ,0,domainName,serverName,varGetReqCompl)
      varGetThrIdles = str(cmo.getExecuteThreadIdleCount());              writeToFile("monitorPRD_PER_THREAD_ExecuteThIdleCount"       ,0,domainName,serverName,varGetThrIdles)
      varGetThrTotal = str(cmo.getExecuteThreadTotalCount());             writeToFile("monitorPRD_PER_THREAD_ExecuteThTotalCount"      ,0,domainName,serverName,varGetThrTotal)
      varGetThrHogge = str(cmo.getHoggingThreadCount());                  writeToFile("monitorPRD_PER_THREAD_HoggingThCount"           ,0,domainName,serverName,varGetThrHogge)
      varGetThrPendi = str(cmo.getPendingUserRequestCount());             writeToFile("monitorPRD_PER_THREAD_PendingUserReqCount"      ,0,domainName,serverName,varGetThrPendi)
      varGetThrStand = str(cmo.getStandbyThreadCount());                  writeToFile("monitorPRD_PER_THREAD_StandbyThCount"           ,0,domainName,serverName,varGetThrStand)
      varGetThrThrou = str(cmo.getThroughput());                          writeToFile("monitorPRD_PER_THREAD_Throughput"               ,0,domainName,serverName,varGetThrThrou)
      #------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
      writeToFile("monitorPRD__ALL_HEALTH",0,domainName,serverName, str(varGetServStat)+','+str(varGetSeHealtR)+','+str(varGetSeHealtA)+','+str(varGetHeapMaxm)+','+str(varGetHeapCurr)+','+str(varGetHeapFree)+','+str(varGetHeapTota)+','+str(varGetHeapUsed)+','+str(varGetHeapFPct)+','+str(varGetHeapUPct)+','+str(varGetTimeDayD)+',0,' )
      print('%-25s %-20s %10s %8s %8s %8s %8s %8s %8s %-10s %-10s %-10s' % (domainName,serverName,varGetHeapCurr,varGetHeapFree,varGetHeapMaxm,varGetHeapTota,varGetHeapUsed,varGetHeapFPct,varGetHeapUPct,varGetServStat,varGetSeHealtR,varGetSeHealtA));
      cd("/")
    except Exception, e:
      print '(Except) ACTUAL STATUS [ '+serverName+' ]'
      #logger.error('Failed : '+ str(e))
      print '(Failed) : [ '+str(e)+' ]'
      state(serverName,'Server')
      cd("/")

def allOperations(CONFIG,KEY,ADM,WLURL):
	print('DATE_TIME: '+vNoTIM())
	domainConnect(CONFIG,KEY,ADM,WLURL)
	domainRuntime()
	loadServers=domainRuntimeService.getServerRuntimes();
	if (len(loadServers) > 0):
		print('%-25s %-20s %10s %8s %8s %8s %8s %8s %8s %-10s %-10s %-10s' % ('DOMAIN','SERVER','HeapCurr','HeapFree','HeapMaxm','HeapTota','HeapUsed','HeapFPct','HeapUPct','ServStat','Health_Run','Health_App'))
		for tmpServer in loadServers:
			checkHealth(tmpServer.getName())


def getAppDeploys():
	servers = domainRuntimeService.getServerRuntimes();
	for server in servers:
	
		print('%-20s %-30s' % ('[ APP RUNTIME INFO ]',server.getName()));
		apps = server.getApplicationRuntimes();
		for app in apps:
			varAppGetName = app.getName(); ## print 'Application: ' + app.getName();
			crs = app.getComponentRuntimes();
			for cr in crs:
				varCrGetType = cr.getType(); ## print '-Component Type: ' + cr.getType();
				
				## ----------------------------------------------------------------------------------------------------------------------------------------------------------- ##
				if (varCrGetType == 'EJBComponentRuntime'):
					ejbRTs = cr.getEJBRuntimes();
					for ejbRT in ejbRTs:

						varEJBGetName = ejbRT.getName(); ## print ' -EJBRunTime: ' + ejbRT.getName();
						varEJBGetType = ejbRT.getType(); ## print ' -EJBType ' + ejbRT.getType();

						varEJB_NameRn = ejbRT.getEJBName();
						varEJB_TypeRn = ejbRT.getType();
						varEJB_Titles = str(varEJBGetName) +','+ str(varEJBGetType) +','+ str(varEJB_NameRn) +','+ str(varEJB_TypeRn)                                          # print '    EJB:Module [' + ejbRT.getName() + '] EJB:Type [' + varEJB_TypeRn + ']' + '] EJB:RunName [' + varEJB_NameRn + ']'

						## --------------------------------------------------------------------------------------------------------------------------------------------------- ##
						
						if varEJB_TypeRn == 'EntityEJBRuntime':
							myTxRuntime = ejbRT.getTransactionRuntime();                       # getTransactionRuntime information from TransactionRuntime                     # print vToSTR(myTxRuntime.getTransactionsCommittedTotalCount()) + vToSTR(myTxRuntime.getTransactionsRolledBackTotalCount()) + vToSTR(myTxRuntime.getTransactionsTimedOutTotalCount())
							writeToFile("monitorPRD___RUNTIME_EJB_TransactionRuntime",         0,domainName,server.getName(), varEJB_Titles + ',TransactionRuntime,'           + vToSTR(myTxRuntime.getTransactionsCommittedTotalCount()) +','+ vToSTR(myTxRuntime.getTransactionsRolledBackTotalCount()) +',' + vToSTR(myTxRuntime.getTransactionsTimedOutTotalCount()) )
							
						elif varEJB_TypeRn == 'StatelessEJBRuntime':
							myTxRuntime = ejbRT.getTransactionRuntime();                       # getTransactionRuntime information from TransactionRuntime                     # print vToSTR(myTxRuntime.getTransactionsCommittedTotalCount()) + vToSTR(myTxRuntime.getTransactionsRolledBackTotalCount()) + vToSTR(myTxRuntime.getTransactionsTimedOutTotalCount())
							writeToFile("monitorPRD___RUNTIME_EJB_TransactionRuntime",         0,domainName,server.getName(), varEJB_Titles + ',TransactionRuntime,'           + vToSTR(myTxRuntime.getTransactionsCommittedTotalCount()) +','+ vToSTR(myTxRuntime.getTransactionsRolledBackTotalCount()) +',' + vToSTR(myTxRuntime.getTransactionsTimedOutTotalCount()) )
							
							myPoolRuntime = ejbRT.getPoolRuntime();                            # getPoolRuntime information from PoolRuntime							       # print vToSTR(myPoolRuntime.getAccessTotalCount()) + vToSTR(myPoolRuntime.getBeansInUseCount()) + vToSTR(myPoolRuntime.getBeansInUseCurrentCount()) + vToSTR(myPoolRuntime.getDestroyedTotalCount()) + vToSTR(myPoolRuntime.getIdleBeansCount()) + vToSTR(myPoolRuntime.getPooledBeansCurrentCount()) + vToSTR(myPoolRuntime.getTimeoutTotalCount())
							writeToFile("monitorPRD___RUNTIME_EJB_PoolRuntime",                0,domainName,server.getName(), varEJB_Titles + ',PoolRuntime,'                  + vToSTR(myPoolRuntime.getAccessTotalCount()) +','+ vToSTR(myPoolRuntime.getBeansInUseCount()) +','+ vToSTR(myPoolRuntime.getBeansInUseCurrentCount()) +','+ vToSTR(myPoolRuntime.getDestroyedTotalCount()) +','+ vToSTR(myPoolRuntime.getIdleBeansCount()) +','+ vToSTR(myPoolRuntime.getPooledBeansCurrentCount()) +','+ vToSTR(myPoolRuntime.getTimeoutTotalCount()))
							
							myTimerRuntime = ejbRT.getTimerRuntime();                          # getTimerRuntime consists of a list of timers                                  # if() print myTimerRuntime.getName() + vToSTR(myTimerRuntime.getActiveTimerCount()) + vToSTR(myTimerRuntime.getTimeoutCount()) + vToSTR(myTimerRuntime.getCancelledTimerCount()) + vToSTR(myTimerRuntime.getDisabledTimerCount())
							if myTimerRuntime != None:                                         #                                                                               #
								writeToFile("monitorPRD___RUNTIME_EJB_TimerRuntime",           0,domainName,server.getName(), varEJB_Titles + ',TimerRuntime,'                 + vToSTR(myTimerRuntime.getName()) +','+ vToSTR(myTimerRuntime.getActiveTimerCount()) +','+ vToSTR(myTimerRuntime.getTimeoutCount()) +','+ vToSTR(myTimerRuntime.getCancelledTimerCount()) +','+ vToSTR(myTimerRuntime.getDisabledTimerCount()))
								
						elif varEJB_TypeRn == 'StatefulEJBRuntime':
							myTxRuntime = ejbRT.getTransactionRuntime();                       # getTransactionRuntime information from TransactionRuntime                     # print vToSTR(myTxRuntime.getTransactionsCommittedTotalCount()) + vToSTR(myTxRuntime.getTransactionsRolledBackTotalCount()) + vToSTR(myTxRuntime.getTransactionsTimedOutTotalCount())
							writeToFile("monitorPRD___RUNTIME_EJB_TransactionRuntime",         0,domainName,server.getName(), varEJB_Titles + ',TransactionRuntime,'           + vToSTR(myTxRuntime.getTransactionsCommittedTotalCount()) +','+ vToSTR(myTxRuntime.getTransactionsRolledBackTotalCount()) +',' + vToSTR(myTxRuntime.getTransactionsTimedOutTotalCount()) )
							
							myCacheRuntime = ejbRT.getCacheRuntime();                          # getCacheRuntime information from CacheRuntime                                 # print vToSTR(myCacheRuntime.getCacheHitCount()) + vToSTR(myCacheRuntime.getCachedBeansCurrentCount()) + vToSTR(myCacheRuntime.getCacheAccessCount())
							writeToFile("monitorPRD___RUNTIME_EJB_CacheRuntime",               0,domainName,server.getName(), varEJB_Titles + ',CacheRuntime,'                 + vToSTR(myCacheRuntime.getCacheHitCount()) +','+ vToSTR(myCacheRuntime.getCachedBeansCurrentCount()) +','+ vToSTR(myCacheRuntime.getCacheAccessCount()) )
							
							myLockingRuntime = ejbRT.getLockingRuntime();                      # getLockingRuntime information from LockingRuntime                             # print vToSTR(myLockingRuntime.getLockEntriesCurrentCount()) + vToSTR(myLockingRuntime.getLockManagerAccessCount()) + vToSTR(myLockingRuntime.getTimeoutTotalCount())
							writeToFile("monitorPRD___RUNTIME_EJB_LockingRuntime",             0,domainName,server.getName(), varEJB_Titles + ',LockingRuntime,'               + vToSTR(myLockingRuntime.getLockEntriesCurrentCount()) +','+ vToSTR(myLockingRuntime.getLockManagerAccessCount()) +','+ vToSTR(myLockingRuntime.getTimeoutTotalCount()) )

						elif varEJB_TypeRn == 'MessageDrivenEJBRuntime':
							myTxRuntime = ejbRT.getTransactionRuntime()                        # getTransactionRuntime information from TransactionRuntime                     # print vToSTR(myTxRuntime.getTransactionsCommittedTotalCount()) + vToSTR(myTxRuntime.getTransactionsRolledBackTotalCount()) + vToSTR(myTxRuntime.getTransactionsTimedOutTotalCount())
							writeToFile("monitorPRD___RUNTIME_EJB_TransactionRuntime",         0,domainName,server.getName(), varEJB_Titles + ',TransactionRuntime,'           + vToSTR(myTxRuntime.getTransactionsCommittedTotalCount()) +','+ vToSTR(myTxRuntime.getTransactionsRolledBackTotalCount()) +',' + vToSTR(myTxRuntime.getTransactionsTimedOutTotalCount()) )
							
							myTxMDBStatus = ejbRT.getMDBStatus();                              # getMDBStatus                                                                  # print
							myTxMDBHealth = str(repr(ejbRT.getHealthState()));                 # getHealthState                                                                # print
							if ("HEALTH_OK" in str(myTxMDBHealth)): myTxMDBHealth = 'HEALTH_OK';
							else: myTxMDBHealth = 'HEALTH_ERROR'
							writeToFile("monitorPRD___RUNTIME_EJB_MDBinfo",                    0,domainName,server.getName(), varEJB_Titles + ',EJB_MDB,'                      + vToSTR(myTxMDBStatus) +',' + vToSTR(myTxMDBHealth) )
				
				## ----------------------------------------------------------------------------------------------------------------------------------------------------------- ##
				if (varCrGetType == 'WebAppComponentRuntime'):
					varWEBGetNameApp = cr.getName();                                        # print ' -Name: ' + cr.getName();
					varWEBGet_InfoUP = vToSTR(varAppGetName) +','+ vToSTR(varCrGetType) +','+ vToSTR(varWEBGetNameApp)
					
					varWEBGet_Detail = varWEBGet_InfoUP;
					varWEBGet_Detail += ',' + vToSTR(cr.getModuleURI());                       # (String) Returns the web-uri as configured in application.xml for the webapp.
					varWEBGet_Detail += ',' + vToSTR(repr(cr.getOpenSessionsCurrentCount()));  #    (int) Provides a count of the current total number of open sessions in this module.
					varWEBGet_Detail += ',' + vToSTR(cr.getOpenSessionsHighCount());           #    (int) Provides the high water mark of the total number of open sessions in this server
					varWEBGet_Detail += ',' + vToSTR(cr.getSessionsOpenedTotalCount());        #    (int) Provides a count of the total number of sessions opened.
					varWEBGet_Detail += ',' + vToSTR(cr.getSessionTimeoutSecs());              #    (int) Provides the timeout configured for http sessions. 
					varWEBGet_Detail += ',' + vToSTR(cr.getSingleThreadedServletPoolSize());   #    (int) Provides the single threaded servlet pool size as it is configured in weblogic.xml.
					varWEBGet_Detail += ',' + vToSTR(cr.getSourceInfo());                      # (String) Provides an informative string about the module's source.
					varWEBGet_Detail += ',' + vToSTR(cr.getStatus());                          # (String) Provides the status of the component.
					varWEBGet_Detail += ',' + vToSTR(cr.getWebPubSubRuntime());                # (String) Get Http Pub/Sub Server Runtime of this webapp
					writeToFile("monitorPRD___RUNTIME_WEB",0,domainName,server.getName(),varWEBGet_Detail)

					servlets = cr.getServlets();
					for servlet in servlets:
						varServletConcat  = vToSTR(servlet.getServletName());                  # (String) Provides the name of this instance of a servlet.
						varServletConcat += ',' + vToSTR(servlet.getContextPath());            # (String) Provides the context path for this servlet.
						varServletConcat += ',' + vToSTR(servlet.getServletPath());            # (String) Provides the servlet path.
						varServletConcat += ',' + vToSTR(servlet.getURL());                    # (String) Provides the value of the URL for this servlet.
						varServletConcat += ',' + vToSTR(servlet.getServletClassName());       # (String) Provides the servlet class name
						varServletConcat += ',' + vToSTR(servlet.getExecutionTimeAverage());   #    (int) Provides the average amount of time all invocations of the servlet have executed since created.
						varServletConcat += ',' + vToSTR(servlet.getExecutionTimeHigh());      #    (int) Provides the amount of time the single longest invocation of the servlet has executed since created.
						varServletConcat += ',' + vToSTR(servlet.getExecutionTimeLow());       #    (int) Provides the amount of time the single shortest invocation of the servlet has executed since created.
						varServletConcat += ',' + vToSTR(servlet.getExecutionTimeTotal());     #   (long) Provides the total amount of time all invocations of the servlet have executed since created.
						varServletConcat += ',' + vToSTR(servlet.getInvocationTotalCount());   #    (int) Provides a total count of the times this servlet has been invoked.
						varServletConcat += ',' + vToSTR(servlet.getPoolMaxCapacity());        #    (int) Provides the maximum capacity of this servlet for single thread model servlets.
						varServletConcat += ',' + vToSTR(servlet.getReloadTotalCount());       #    (int) Provides a total count of the number of times this servlet has been reloaded.
						writeToFile("monitorPRD___RUNTIME_WEB_Servlets",0,domainName,server.getName(), varWEBGet_InfoUP+','+varServletConcat )

		print('%-20s %-30s' % ('[ JMS RUNTIME INFO ]',server.getName()));
		try:
			jmsRuntime = server.getJMSRuntime();
			connections = jmsRuntime.getConnections();
			try:
				for connection in connections:                              # print('-Connection Name: ' + connection.getName());
					sessions = connection.getSessions();
					for session in sessions:                                # print(' -Session Name: ' + session.getName());
						varJMS_TValues = str(connection.getName()) +','+ str(session.getName());
						## ----------------------------- ##
						consumers = session.getConsumers();
						for consumer in consumers:                          # print('  -Consumer Name: ' + consumer.getName() + ', Bytes Received: ' + repr(consumer.getBytesReceivedCount()));
							if (repr(consumer.getBytesReceivedCount()) != '0L'):
								VAR_getBytesRec = repr(consumer.getBytesReceivedCount()); VAR_getBytesRec = VAR_getBytesRec.replace('L', '');
								writeToFile("monitorPRD___RUNTIME_JMS_TxBytes", 0,domainName,server.getName(), varJMS_TValues +',JMS_CONSUMER,'+ str(consumer.getName()) +',BYTES_RECEIVED,'+ VAR_getBytesRec )
						## ----------------------------- ##
						producers = session.getProducers();
						for producer in producers:                          # print('  -Producer Name: ' + producer.getName() + ', Bytes Send: ' + repr(producer.getBytesSentCount()));
							if (repr(producer.getBytesSentCount()) != '0L'):
								VAR_getBytesSen = repr(producer.getBytesSentCount()); VAR_getBytesSen = VAR_getBytesSen.replace('L', '');
								writeToFile("monitorPRD___RUNTIME_JMS_TxBytes", 0,domainName,server.getName(), varJMS_TValues +',JMS_PRODUCER,'+ str(producer.getName()) +',BYTES_SEND,'+ VAR_getBytesSen )
				cd("/")
			except:
				## writeToFile("monitorPRD___RUNTIME_JMS_TxBytes", 0,domainName,server.getName(), 'ERROR_JMS_SessionNotFoundException' );
				print('%-20s %-30s' % ('[    (ERROR[2])    ]',server.getName()));
		except:
			## writeToFile("monitorPRD___RUNTIME_JMS_TxBytes", 0,domainName,server.getName(), 'ERROR_JMS_InstanceNotFoundException' );
			print('%-20s %-30s' % ('[    (ERROR[1])    ]',server.getName()));
	print('%-20s %-30s' % ('[ APP RUNTIME DONE ]',domainName));

def getDataSources():
	allServers=domainRuntimeService.getServerRuntimes();
	if (len(allServers) > 0):
	  for tempServer in allServers:
		jdbcServiceRT = tempServer.getJDBCServiceRuntime();
		dataSources = jdbcServiceRT.getJDBCDataSourceRuntimeMBeans();
		if (len(dataSources) > 0):
			for dataSource in dataSources:
				strDSO  =       vToSTR(dataSource.getName())                              ##; print 'Name                               ' , dataSource.getName()
				strDSO += ',' + vToSTR(dataSource.getState())                             ##; print 'State                              ' , dataSource.getState()
				strDSO += ',' + vToSTR(dataSource.getActiveConnectionsAverageCount())     ##; print 'ActiveConnectionsAverageCount      ' , dataSource.getActiveConnectionsAverageCount()
				strDSO += ',' + vToSTR(dataSource.getActiveConnectionsCurrentCount())     ##; print 'ActiveConnectionsCurrentCount      ' , dataSource.getActiveConnectionsCurrentCount()
				strDSO += ',' + vToSTR(dataSource.getActiveConnectionsHighCount())        ##; print 'ActiveConnectionsHighCount         ' , dataSource.getActiveConnectionsHighCount()
				strDSO += ',' + vToSTR(dataSource.getConnectionDelayTime())               ##; print 'ConnectionDelayTime                ' , dataSource.getConnectionDelayTime()
				strDSO += ',' + vToSTR(dataSource.getConnectionsTotalCount())             ##; print 'ConnectionsTotalCount              ' , dataSource.getConnectionsTotalCount()
				strDSO += ',' + vToSTR(dataSource.getCurrCapacity())                      ##; print 'CurrCapacity                       ' , dataSource.getCurrCapacity()
				strDSO += ',' + vToSTR(dataSource.getCurrCapacityHighCount())             ##; print 'CurrCapacityHighCount              ' , dataSource.getCurrCapacityHighCount()
				strDSO += ',' + vToSTR(dataSource.getDeploymentState())                   ##; print 'DeploymentState                    ' , dataSource.getDeploymentState()
				strDSO += ',' + vToSTR(dataSource.getFailedReserveRequestCount())         ##; print 'FailedReserveRequestCount          ' , dataSource.getFailedReserveRequestCount()
				strDSO += ',' + vToSTR(dataSource.getFailuresToReconnectCount())          ##; print 'FailuresToReconnectCount           ' , dataSource.getFailuresToReconnectCount()
				strDSO += ',' + vToSTR(dataSource.getHighestNumAvailable())               ##; print 'HighestNumAvailable                ' , dataSource.getHighestNumAvailable()
				strDSO += ',' + vToSTR(dataSource.getHighestNumUnavailable())             ##; print 'HighestNumUnavailable              ' , dataSource.getHighestNumUnavailable()
				strDSO += ',' + vToSTR(dataSource.getLeakedConnectionCount())             ##; print 'LeakedConnectionCount              ' , dataSource.getLeakedConnectionCount()
				strDSO += ',' + vToSTR(dataSource.getModuleId())                          ##; print 'ModuleId                           ' , dataSource.getModuleId()
				strDSO += ',' + vToSTR(dataSource.getNumAvailable())                      ##; print 'NumAvailable                       ' , dataSource.getNumAvailable()
				strDSO += ',' + vToSTR(dataSource.getNumUnavailable())                    ##; print 'NumUnavailable                     ' , dataSource.getNumUnavailable()
				strDSO += ',' + vToSTR(dataSource.getParent())                            ##; print 'Parent                             ' , dataSource.getParent()
				strDSO += ',' + vToSTR(dataSource.getPrepStmtCacheAccessCount())          ##; print 'PrepStmtCacheAccessCount           ' , dataSource.getPrepStmtCacheAccessCount()
				strDSO += ',' + vToSTR(dataSource.getPrepStmtCacheAddCount())             ##; print 'PrepStmtCacheAddCount              ' , dataSource.getPrepStmtCacheAddCount()
				strDSO += ',' + vToSTR(dataSource.getPrepStmtCacheCurrentSize())          ##; print 'PrepStmtCacheCurrentSize           ' , dataSource.getPrepStmtCacheCurrentSize()
				strDSO += ',' + vToSTR(dataSource.getPrepStmtCacheDeleteCount())          ##; print 'PrepStmtCacheDeleteCount           ' , dataSource.getPrepStmtCacheDeleteCount()
				strDSO += ',' + vToSTR(dataSource.getPrepStmtCacheHitCount())             ##; print 'PrepStmtCacheHitCount              ' , dataSource.getPrepStmtCacheHitCount()
				strDSO += ',' + vToSTR(dataSource.getPrepStmtCacheMissCount())            ##; print 'PrepStmtCacheMissCount             ' , dataSource.getPrepStmtCacheMissCount()
				strDSO += ',' + vToSTR(dataSource.getProperties())                        ##; print 'Properties                         ' , str(dataSource.getProperties()).replace(",", "")
				strDSO += ',' + vToSTR(dataSource.getReserveRequestCount())               ##; print 'ReserveRequestCount                ' , dataSource.getReserveRequestCount()
				strDSO += ',' + vToSTR(dataSource.getType())                              ##; print 'Type                               ' , dataSource.getType()
				strDSO += ',' + vToSTR(dataSource.getVersionJDBCDriver())                 ##; print 'VersionJDBCDriver                  ' , dataSource.getVersionJDBCDriver()
				strDSO += ',' + vToSTR(dataSource.getWaitingForConnectionCurrentCount())  ##; print 'WaitingForConnectionCurrentCount   ' , dataSource.getWaitingForConnectionCurrentCount()
				strDSO += ',' + vToSTR(dataSource.getWaitingForConnectionFailureTotal())  ##; print 'WaitingForConnectionFailureTotal   ' , dataSource.getWaitingForConnectionFailureTotal()
				strDSO += ',' + vToSTR(dataSource.getWaitingForConnectionHighCount())     ##; print 'WaitingForConnectionHighCount      ' , dataSource.getWaitingForConnectionHighCount()
				strDSO += ',' + vToSTR(dataSource.getWaitingForConnectionSuccessTotal())  ##; print 'WaitingForConnectionSuccessTotal   ' , dataSource.getWaitingForConnectionSuccessTotal()
				strDSO += ',' + vToSTR(dataSource.getWaitingForConnectionTotal())         ##; print 'WaitingForConnectionTotal          ' , dataSource.getWaitingForConnectionTotal()
				strDSO += ',' + vToSTR(dataSource.getWaitSecondsHighCount())              ##; print 'WaitSecondsHighCount               ' , dataSource.getWaitSecondsHighCount()
				
				writeToFile("monitorPRD___SERVICE_DSO",0,domainName,tempServer.getName(),strDSO)
	print('%-20s %-30s' % ('[  DS SERVICE DONE ]',domainName));

def getDataJMS():
	servers = domainRuntimeService.getServerRuntimes();
	if (len(servers) > 0):
		for server in servers:
			jmsRuntime = server.getJMSRuntime();
			jmsServers = jmsRuntime.getJMSServers();
			for jmsServer in jmsServers:
				destinations = jmsServer.getDestinations();
				for destination in destinations:
					try:
						strJMS  =       vToSTR(jmsServer.getName());                           ## print ' JMSServer                   ' ,  vToSTR(jmsServer.getName())
						strJMS += ',' + vToSTR(destination.getName());                         ## print ' Name                        ' ,  vToSTR(destination.getName())
						strJMS += ',' + vToSTR(destination.getType());                         ## print ' Type                        ' ,  vToSTR(destination.getType())
						strJMS += ',' + vToSTR(destination.getState());                        ## print ' State                       ' ,  vToSTR(destination.getState())
						strJMS += ',' + vToSTR(destination.getParent());                       ## print ' Parent                      ' ,  vToSTR(destination.getParent())
						strJMS += ',' + vToSTR(destination.getMessagesCurrentCount());         ## print ' MessagesCurrentCount        ' ,  vToSTR(destination.getMessagesCurrentCount())
						strJMS += ',' + vToSTR(destination.getMessagesDeletedCurrentCount());  ## print ' MessagesDeletedCurrentCount ' ,  vToSTR(destination.getMessagesDeletedCurrentCount())
						strJMS += ',' + vToSTR(destination.getMessagesHighCount());            ## print ' MessagesHighCount           ' ,  vToSTR(destination.getMessagesHighCount())
						strJMS += ',' + vToSTR(destination.getMessagesMovedCurrentCount());    ## print ' MessagesMovedCurrentCount   ' ,  vToSTR(destination.getMessagesMovedCurrentCount())
						strJMS += ',' + vToSTR(destination.getMessagesPendingCount());         ## print ' MessagesPendingCount        ' ,  vToSTR(destination.getMessagesPendingCount())
						strJMS += ',' + vToSTR(destination.getMessagesReceivedCount());        ## print ' MessagesReceivedCount       ' ,  vToSTR(destination.getMessagesReceivedCount())
						strJMS += ',' + vToSTR(destination.getMessagesThresholdTime());        ## print ' MessagesThresholdTime       ' ,  vToSTR(destination.getMessagesThresholdTime())
						strJMS += ',' + vToSTR(destination.getDestinationInfo());              ## print ' DestinationInfo             ' ,  vToSTR(destination.getDestinationInfo())
						strJMS += ',' + vToSTR(destination.getDestinationType());              ## print ' DestinationType             ' ,  vToSTR(destination.getDestinationType())
						strJMS += ',' + vToSTR(destination.isInsertionPaused());               ## print ' InsertionPaused             ' ,  vToSTR(destination.isInsertionPaused())
						strJMS += ',' + vToSTR(destination.getInsertionPausedState());         ## print ' InsertionPausedState        ' ,  vToSTR(destination.getInsertionPausedState())
						strJMS += ',' + vToSTR(destination.isPaused());                        ## print ' Paused                      ' ,  vToSTR(destination.isPaused())
						strJMS += ',' + vToSTR(destination.isProductionPaused());              ## print ' ProductionPaused            ' ,  vToSTR(destination.isProductionPaused())
						strJMS += ',' + vToSTR(destination.getProductionPausedState());        ## print ' ProductionPausedState       ' ,  vToSTR(destination.getProductionPausedState())
						strJMS += ',' + vToSTR(destination.getBytesCurrentCount());            ## print ' BytesCurrentCount           ' ,  vToSTR(destination.getBytesCurrentCount())
						strJMS += ',' + vToSTR(destination.getBytesHighCount());               ## print ' BytesHighCount              ' ,  vToSTR(destination.getBytesHighCount())
						strJMS += ',' + vToSTR(destination.getBytesPendingCount());            ## print ' BytesPendingCount           ' ,  vToSTR(destination.getBytesPendingCount())
						strJMS += ',' + vToSTR(destination.getBytesReceivedCount());           ## print ' BytesReceivedCount          ' ,  vToSTR(destination.getBytesReceivedCount())
						strJMS += ',' + vToSTR(destination.getBytesThresholdTime());           ## print ' BytesThresholdTime          ' ,  vToSTR(destination.getBytesThresholdTime())
						strJMS += ',' + vToSTR(destination.getConsumersCurrentCount());        ## print ' ConsumersCurrentCount       ' ,  vToSTR(destination.getConsumersCurrentCount())
						strJMS += ',' + vToSTR(destination.getConsumersHighCount());           ## print ' ConsumersHighCount          ' ,  vToSTR(destination.getConsumersHighCount())
						strJMS += ',' + vToSTR(destination.getConsumersTotalCount());          ## print ' ConsumersTotalCount         ' ,  vToSTR(destination.getConsumersTotalCount())
						strJMS += ',' + vToSTR(destination.getConsumptionPausedState());       ## print ' ConsumptionPausedState      ' ,  vToSTR(destination.getConsumptionPausedState())
						writeToFile("monitorPRD___SERVICE_JMS",0,domainName,server.getName(),strJMS)
					except:
						print 'ERROR_DATA';
	print('%-20s %-30s' % ('[ JMS SERVICE DONE ]',domainName));


def writeToFile(FILE,INT,DOMAIN,SERVER,VALUE):
	fileToWrite=open("/oracle/control/check_fmw_services/FILES/"+FILE+".csv","a+")
	# fileToWrite.write("%s,%d,%s,%s\r\n" % (DOMAIN, INT, SERVER, VALUE))
	if(INT == 999):
		fileToWrite.write("%s,%s,%s,%s\r\n" % (DOMAIN, 'Date',   SERVER, VALUE))
	else:
		fileToWrite.write("%s,%s,%s,%s\r\n" % (DOMAIN, vNoTIM(), SERVER, VALUE))
	fileToWrite.close()

def resetOfFiles():
	import glob
	path = '/oracle/control/check_fmw_services/FILES'
	FILESTORESET = [f for f in glob.glob(path + "**/*.csv")]
	for varFileToReset in FILESTORESET:
		if (".ERROR." in str(varFileToReset)):
			print 'SKIPPED>' + varFileToReset
		else:
			fileToReset=open(varFileToReset,"w")
			fileToReset.close()

def titleOfFiles():
	strTit_HLT  = 'State,Health,Status,HEAP_Maximum,HEAP_Current,HEAP_Free,HEAP_Total,HEAP_Used,HEAP_Pct_Free,HEAP_Pct_Used,UP_Time'
	strTit_HLT += ',Extra_001'
	writeToFile("monitorPRD__ALL_HEALTH",                        999,'DomainName','ServerName',strTit_HLT)

	strTit_DSO  = 'Name,State,ActiveConnectionsAverageCount,ActiveConnectionsCurrentCount,ActiveConnectionsHighCount,ConnectionDelayTime,ConnectionsTotalCount'
	strTit_DSO += ',CurrCapacity,CurrCapacityHighCount,DeploymentState,FailedReserveRequestCount,FailuresToReconnectCount,HighestNumAvailable,HighestNumUnavailable'
	strTit_DSO += ',LeakedConnectionCount,ModuleId,NumAvailable,NumUnavailable,Parent,PrepStmtCacheAccessCount,PrepStmtCacheAddCount,PrepStmtCacheCurrentSize'
	strTit_DSO += ',PrepStmtCacheDeleteCount,PrepStmtCacheHitCount,PrepStmtCacheMissCount,Properties,ReserveRequestCount,Type,VersionJDBCDriver'
	strTit_DSO += ',WaitingForConnectionCurrentCount,WaitingForConnectionFailureTotal,WaitingForConnectionHighCount,WaitingForConnectionSuccessTotal'
	strTit_DSO += ',WaitingForConnectionTotal,WaitSecondsHighCount'
	writeToFile("monitorPRD___SERVICE_DSO",                      999,'DomainName','ServerName',strTit_DSO)

	strTit_JMS  = 'JMSServer,Name,Type,State,Parent,MessagesCurrentCount,MessagesDeletedCurrentCount,MessagesHighCount,MessagesMovedCurrentCount'
	strTit_JMS += ',MessagesPendingCount,MessagesReceivedCount,MessagesThresholdTime,DestinationInfo,DestinationType,InsertionPaused'
	strTit_JMS += ',InsertionPausedState,Paused,ProductionPaused,ProductionPausedState,BytesCurrentCount,BytesHighCount,BytesPendingCount'
	strTit_JMS += ',BytesReceivedCount,BytesThresholdTime,ConsumersCurrentCount,ConsumersHighCount,ConsumersTotalCount,ConsumptionPausedState'
	writeToFile("monitorPRD___SERVICE_JMS",                      999,'DomainName','ServerName',strTit_JMS)
	
	strTit_EJB  = 'EJB_Name,EJBType,EJB_NameRn,EJB_TypeRn,EJB_SubType'
	writeToFile("monitorPRD___RUNTIME_EJB_TransactionRuntime",   999,'DomainName','ServerName',strTit_EJB + ',TxCommittedTotalCount,TxRolledBackTotalCount,TxTimedOutTotalCount')
	writeToFile("monitorPRD___RUNTIME_EJB_PoolRuntime",          999,'DomainName','ServerName',strTit_EJB + ',PoolRn.AccessTot,PoolRn.BeansInUseCount,PoolRn.BeansInUseCurrentCount,PoolRn.DestroyedTot,PoolRn.IdleBeansCount,PoolRn.PooledBeansCurrentCount,PoolRn.TimeoutTot')
	writeToFile("monitorPRD___RUNTIME_EJB_TimerRuntime",         999,'DomainName','ServerName',strTit_EJB + ',TimRn.Name,TimRn.ActiveTimerCount,TimRn.TimeoutCount,TimRn.CancelledTimerCount,TimRn.DisabledTimerCount')
	writeToFile("monitorPRD___RUNTIME_EJB_CacheRuntime",         999,'DomainName','ServerName',strTit_EJB + ',CacheRn.CacheHitCount,CacheRn.CachedBeansCurrentCount,CacheRn.CacheAccessCount')
	writeToFile("monitorPRD___RUNTIME_EJB_LockingRuntime",       999,'DomainName','ServerName',strTit_EJB + ',LockRn.LockEntriesCurrentCount,LockRn.LockManagerAccessCount,LockRn.TimeoutTotalCount')
	writeToFile("monitorPRD___RUNTIME_EJB_MDBinfo",              999,'DomainName','ServerName',strTit_EJB + ',TxMDBStatus,TxMDBHealth')
	
	strRUN_WEB  = 'AppName,AppCrType,WEB_AppName'
	strRUN_WEBMain = strRUN_WEB + ',ModuleURI,OpenSessionsCurrentCount,OpenSessionsHighCount,SessionsOpenedTotalCount,SessionTimeoutSecs,SingleThreadedServletPoolSize,SourceInfo,Status,WebPubSubRuntime'
	strRUN_WEBServ = strRUN_WEB + ',ServletName,ContextPath,ServletPath,URL,ServletClassName,ExecutionTimeAverage,ExecutionTimeHigh,ExecutionTimeLow,ExecutionTimeTotal,InvocationTotalCount,PoolMaxCapacity,ReloadTotalCount'
	writeToFile("monitorPRD___RUNTIME_WEB",                      999,'DomainName','ServerName',strRUN_WEBMain)
	writeToFile("monitorPRD___RUNTIME_WEB_Servlets",             999,'DomainName','ServerName',strRUN_WEBServ)

	strRUN_JMS  = 'Connection_Name,Session_Name,JMS_Type,JMS_Name,JMS_Tx,BytesCount'
	writeToFile("monitorPRD___RUNTIME_JMS_TxBytes",              999,'DomainName','ServerName',strRUN_JMS)

resetOfFiles()
titleOfFiles()


allOperations('/oracle/control/check_fmw/keystore/BIP-RMS_wl_config'  ,'/oracle/control/check_fmw/keystore/BIP-RMS_wl_key'  ,'AdminServer'  ,'t3://172.16.11.7:11001');   disconnect(); print; print;
allOperations('/oracle/control/check_fmw/keystore/BIP-SIM_wl_config'  ,'/oracle/control/check_fmw/keystore/BIP-SIM_wl_key'  ,'AdminServer'  ,'t3://172.16.11.22:11001');  disconnect(); print; print;
allOperations('/oracle/control/check_fmw/keystore/OID_wl_config'      ,'/oracle/control/check_fmw/keystore/OID_wl_key'      ,'AdminServer'  ,'t3://172.16.11.3:7001');    disconnect(); print; print;
allOperations('/oracle/control/check_fmw/keystore/RDF_wl_config'      ,'/oracle/control/check_fmw/keystore/RDF_wl_key'      ,'AdminServer'  ,'t3://172.16.11.20:7001');   disconnect(); print; print;
allOperations('/oracle/control/check_fmw/keystore/REIM_wl_config'     ,'/oracle/control/check_fmw/keystore/REIM_wl_key'     ,'AdminServer'  ,'t3://172.16.11.23:9001');   disconnect(); print; print;
allOperations('/oracle/control/check_fmw/keystore/RESA_wl_config'     ,'/oracle/control/check_fmw/keystore/RESA_wl_key'     ,'AdminServer'  ,'t3://172.16.11.25:8001');   disconnect(); print; print;
allOperations('/oracle/control/check_fmw/keystore/RFI_wl_config'      ,'/oracle/control/check_fmw/keystore/RFI_wl_key'      ,'AdminServer'  ,'t3://172.16.11.16:17001');  disconnect(); print; print;
allOperations('/oracle/control/check_fmw/keystore/RIB_wl_config'      ,'/oracle/control/check_fmw/keystore/RIB_wl_key'      ,'AdminServer'  ,'t3://172.16.11.17:7001');   disconnect(); print; print;
allOperations('/oracle/control/check_fmw/keystore/RMS_wl_config'      ,'/oracle/control/check_fmw/keystore/RMS_wl_key'      ,'AdminServer'  ,'t3://172.16.11.1:7001');    disconnect(); print; print;
allOperations('/oracle/control/check_fmw/keystore/RPM_wl_config'      ,'/oracle/control/check_fmw/keystore/RPM_wl_key'      ,'AdminServer'  ,'t3://172.16.11.9:10001');   disconnect(); print; print;
allOperations('/oracle/control/check_fmw/keystore/SIM_wl_config'      ,'/oracle/control/check_fmw/keystore/SIM_wl_key'      ,'AdminServer'  ,'t3://172.16.11.8:7001');    disconnect(); print; print;
allOperations('/oracle/control/check_fmw/keystore/SOA-CRT_wl_config'  ,'/oracle/control/check_fmw/keystore/SOA-CRT_wl_key'  ,'AdminServer'  ,'t3://172.16.11.11:7001');   disconnect(); print; print;
allOperations('/oracle/control/check_fmw/keystore/SOA-GNR_wl_config'  ,'/oracle/control/check_fmw/keystore/SOA-GNR_wl_key'  ,'AdminServer'  ,'t3://172.16.11.10:7101');   disconnect(); print; print;
allOperations('/oracle/control/check_fmw/keystore/ODI-CRT_wl_config'  ,'/oracle/control/check_fmw/keystore/ODI-CRT_wl_key'  ,'AdminServer'  ,'t3://172.16.11.19:7001');   disconnect(); print; print;
allOperations('/oracle/control/check_fmw/keystore/ODI-GNR_wl_config'  ,'/oracle/control/check_fmw/keystore/ODI-GNR_wl_key'  ,'AdminServer'  ,'t3://172.16.11.18:7001');   disconnect(); print; print;


















#time.sleep(1);
#domainRuntime()
#disconnect()




