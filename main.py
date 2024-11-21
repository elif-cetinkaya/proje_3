from abc import ABC, abstractmethod
import random

# Abstract Player Class
class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.moves = []  # Hamle geçmişi
    
    @abstractmethod
    def make_move(self):
        pass  # Abstract method for making a move

# Abstract Computer Player Class
class ComputerPlayer(Player):
    def __init__(self, name="Bilgisayar"):
        super().__init__(name)
    
    def make_move(self):
        move = random.choice(["Taş", "Kağıt", "Makas"])
        self.moves.append(move)
        return move

# Human Player Class
class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def make_move(self):
        while True:
            print("\nSeçenekler: Taş, Kağıt, Makas")
            move = input(f"{self.name}, lütfen hamlenizi yapın: ").capitalize()
            if move in ["Taş", "Kağıt", "Makas"]:
                self.moves.append(move)
                return move
            else:
                print("Geçersiz seçim! Lütfen Taş, Kağıt veya Makas yazın.")

# Game Class
class Game:
    def __init__(self, human_player, computer_player):
        self.human_player = human_player
        self.computer_player = computer_player
        self.rounds = 0
    
    def determine_winner(self, human_move, computer_move):
        if human_move == computer_move:
            return "Berabere"
        elif (human_move == "Taş" and computer_move == "Makas") or \
             (human_move == "Kağıt" and computer_move == "Taş") or \
             (human_move == "Makas" and computer_move == "Kağıt"):
            return self.human_player
        else:
            return self.computer_player

    def play_round(self):
        print("\n=== Yeni Tur Başlıyor ===")
        human_move = self.human_player.make_move()
        computer_move = self.computer_player.make_move()
        
        print(f"{self.human_player.name} seçimi: {human_move}")
        print(f"{self.computer_player.name} seçimi: {computer_move}")
        
        winner = self.determine_winner(human_move, computer_move)
        if winner == "Berabere":
            print("Sonuç: Berabere!")
        else:
            print(f"Sonuç: {winner.name} kazandı!")
            winner.score += 1
        
        self.rounds += 1

    def display_scores(self):
        print("\n=== Skor Durumu ===")
        print(f"{self.human_player.name}: {self.human_player.score} puan")
        print(f"{self.computer_player.name}: {self.computer_player.score} puan")
    
    def display_move_history(self):
        print("\n=== Hamle Geçmişi ===")
        print(f"{self.human_player.name} hamleleri: {', '.join(self.human_player.moves)}")
        print(f"{self.computer_player.name} hamleleri: {', '.join(self.computer_player.moves)}")
    
    def play_game(self):
        print("Taş-Kağıt-Makas Oyununa Hoş Geldiniz!")
        while True:
            self.play_round()
            self.display_scores()
            
            choice = input("\nDevam etmek istiyor musunuz? (E/H): ").strip().upper()
            if choice != 'E':
                print("\nOyun Sonlandırılıyor...")
                self.display_scores()
                self.display_move_history()
                print("Oynadığınız için teşekkürler!")
                break

# Main Function
def main():
    print("=== Taş-Kağıt-Makas Oyunu ===")
    player_name = input("Oyuncu adınızı girin: ").strip()
    human_player = HumanPlayer(player_name)
    computer_player = ComputerPlayer()

    game = Game(human_player, computer_player)
    game.play_game()

if __name__ == "__main__":
    main()
