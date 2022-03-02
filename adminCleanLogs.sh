#########################################################
#########################################################
###                                                   ###
### Clean Logs                                        ###
###                                                   ###
#########################################################
#########################################################

ORACLE_ADMINCLEAN__PATHDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
. $ORACLE_ADMINCLEAN__PATHDIR/adminCleanSetEnv.sh

function AdminClean(){
	# - Check every folder of apps servers
	OAC__FIND_FILES=$1/servers/$2/logs

	# - check instance
	if [ -d "$OAC__FIND_FILES" ]
	then
		echo "+-------------------------------------------------------+"
		echo "|" $2" : "
		echo "|" $OAC__FIND_FILES " "
		echo "+-------------------------------------------------------+"
		OAC__FECHA=$(date +%Y/%m/%d_-_%H-%M-%S) 
		OAC__FECH2=$(date +%Y-%m-%d__%H-%M-%S) 
		OAC__DAYS_TO_DELETE=1
		echo "| Date = "$OAC__FECHA
		echo "| Init size = "$(du -hs $OAC__FIND_FILES)

			OAC__FILE_BIG_LOG=$OAC__FIND_FILES/$2.out
			if [ -f "$OAC__FILE_BIG_LOG" ]
			then
				if [[ -n $(find $OAC__FIND_FILES -name "$2.out" -size +1G) ]];
				  then
					cp -f $OAC__FIND_FILES/$2.out $OAC__FIND_FILES/$2_$OAC__FECH2.out00000
					cat /dev/null > $OAC__FILE_BIG_LOG
					echo "|    Clean : $2.out"
				  else
					echo "|    Pass -1GB : $2.out"
				fi
			fi

			OAC__FILE_BIG_LO2=$OAC__FIND_FILES/access.log
			if [ -f "$OAC__FILE_BIG_LO2" ]
			then
				if [[ -n $(find $OAC__FIND_FILES -name "access.log" -size +1G) ]];
				  then
					cp -f $OAC__FIND_FILES/access.log $OAC__FIND_FILES/access_$OAC__FECH2.log00000
					cat /dev/null > $OAC__FILE_BIG_LO2
					echo "|    Clean : access.log"
				  else
					echo "|    Pass -1GB : access.log"
				fi
			fi

			OAC__FILE_BIG_LO3=$OAC__FIND_FILES/$2.log
			if [ -f "$OAC__FILE_BIG_LO3" ]
			then
				if [[ -n $(find $OAC__FIND_FILES -name "$2.log" -size +1G) ]];
				  then
					cp -f $OAC__FIND_FILES/$2.log $OAC__FIND_FILES/$2_$OAC__FECH2.log00000
					cat /dev/null > $OAC__FILE_BIG_LO3
					echo "|    Clean : $2.log"
				  else
					echo "|    Pass -1GB : $2.log"
				fi
			fi


			find $OAC__FIND_FILES -name '*-diagnostic-*' -mtime +$OAC__DAYS_TO_DELETE | sort | uniq
			find $OAC__FIND_FILES -name '*-diagnostic-*' -mtime +$OAC__DAYS_TO_DELETE | sort | uniq | xargs rm -Rf
			echo "|    Delete Logs : *-diagnostic-*"

			find $OAC__FIND_FILES -name '*.out0*' -mtime +$OAC__DAYS_TO_DELETE | sort | uniq
			find $OAC__FIND_FILES -name '*.out0*' -mtime +$OAC__DAYS_TO_DELETE | sort | uniq | xargs rm -Rf
			echo "|    Delete Logs : *$2.out0*"

for h in 1 2 3 4 5 6 7 8 9
do
			find $OAC__FIND_FILES -name '*.out$h*' -mtime +$OAC__DAYS_TO_DELETE | sort | uniq
			find $OAC__FIND_FILES -name '*.out$h*' -mtime +$OAC__DAYS_TO_DELETE | sort | uniq | xargs rm -Rf
			echo "|    Delete Logs : *$2.out$h*"
done

			find $OAC__FIND_FILES -name '*.log0*' -mtime +$OAC__DAYS_TO_DELETE | sort | uniq
			find $OAC__FIND_FILES -name '*.log0*' -mtime +$OAC__DAYS_TO_DELETE | sort | uniq | xargs rm -Rf
			echo "|    Delete Logs : *$2.log0*"

for p in 1 2 3 4 5 6 7 8 9
do
			find $OAC__FIND_FILES -name '*.log$p*' -mtime +$OAC__DAYS_TO_DELETE | sort | uniq
			find $OAC__FIND_FILES -name '*.log$p*' -mtime +$OAC__DAYS_TO_DELETE | sort | uniq | xargs rm -Rf
			echo "|    Delete Logs : *$2.log$p*"
done

		echo "| Final Size   = "$(du -hs $OAC__FIND_FILES)
		echo "+-------------------------------------------------------+"
		echo -e
	else
		# - La Instancia No Existe
		echo -e
	fi
}

OAC__FECHA=$(date +%Y/%m/%d_-_%H-%M-%S)
echo "#########################################################"
echo "## Clean of Logs  ## "$OAC__FECHA" ###########"
echo "#########################################################"
	echo -e
	# echo "*-----------------------------------*"
	# echo "|-> WL Logs Eliminados de: core.* <-|"
	# find $ORACLE_ADMIN__PATH_DOMAIN -name 'core.*' | sort | uniq | xargs rm -Rf
	# echo "*-----------------------------------*"
	# echo -e
	. $ORACLE_ADMINCLEAN__PATHDIR/adminCleanInstancias.sh