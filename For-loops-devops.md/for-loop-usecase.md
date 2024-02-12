servers=("server1" "server2" "server3")
for server in "${server[@]}; do
    configure_monitoring_agent  "$server"
done
