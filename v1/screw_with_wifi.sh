#random=$(read /dev/urandom)
for i in {1..500}
do
	random=$(uuidgen)
	iwconfig wlp2s0 essid "${random:5}"
	sleep 0.5s
	echo "DONE $i"
done
