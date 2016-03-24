require 'websocket-client-simple'

ws = WebSocket::Client::Simple.connect 'ws://localhost:8000'

ws.on :open do
  puts "Socket opened"
end

ws.on :close do |e|
  p e
  exit 1
end

ws.on :error do |e|
  p e
end



loop do
  ws.send "boom!"
  sleep(1)
end

