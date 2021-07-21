import pygame
import random
import sys
from settings import Settings

from pygame.display import update    


class Visualizer:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1000,1000))
        self.nums = []
        for x in range(self.settings.num_val):
            self.nums.append(random.randint(0,self.settings.max_val))

    def quicksort(self,list,first,last):
        if first < last:
            split = self.partition(list,first,last)
            self.quicksort(list,first,split-1)
            self.quicksort(list,split+1,last)


    def partition(self,list,first,last):
        self._check_events()
        pivot = list[last]
        i = first-1
        for j in range(first,last):
            if list[j] < pivot:
                i += 1
                list[i],list[j] = list[j],list[i]
                pygame.time.delay(20)
                self._update_screen()
                self.make_colorbar(list,i)
                self.make_colorbar(list,j)
                pygame.display.update()
                
        list[i+1],list[last] = list[last],list[i+1]
        self._update_screen()
        return i+1

    def selctionsort(self,nums):
        for i in range(0,len(nums)):
            min = nums[i]
            index = i
            for j in range(i,len(nums)):
                if nums[j] < min:
                    min = nums[j]
                    index = j
            
            nums[i], nums[index] = nums[index], nums[i]
            pygame.time.delay(20)
            self._update_screen()
            self.make_colorbar(nums,i)
            self.make_colorbar(nums,index)
            pygame.display.update()
    
    def bubblesort(self,nums,last):
        if last == 0:
            return
        for i in range(0,last):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                pygame.time.delay(20)
                self._update_screen()
                self.make_colorbar(nums,i)
                pygame.display.update()

        self.bubblesort(nums,last-1)

    
    def insertionsort(self,nums):
        for num in range(1,len(nums)):
            i = num
            while nums[i-1] >= nums[num] and i >0:
                i -= 1
            nums.insert(i,nums[num])
            nums.pop(num+1)
            pygame.time.delay(20)
            self._update_screen()
            self.make_colorbar(nums,i)
            pygame.display.update()

    def mergesort(self,nums):
        if len(nums) > 1:
            center = int(len(nums)/2)
            l = nums[:center]
            r = nums[center:]
            self.mergesort(l)
            self.mergesort(r)
            i = j = n = 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    nums[n] = l[i]
                    i += 1 
                else:
                    nums[n] = r[j]
                    j += 1
                n += 1
                pygame.time.delay(20)
                self._update_screen()
            while i < len(l):
                nums[n] = l[i]
                pygame.time.delay(20)
                self._update_screen()
                i += 1
                n += 1
            while j < len(r):
                nums[n] = r[j]
                pygame.time.delay(20)
                self._update_screen()
                j += 1
                n += 1


    def make_bars(self,list):
        width = 1000/self.settings.num_val
        height = 1000/self.settings.max_val
        for x in range(0,len(list)):
            bar = pygame.Rect(x*width,1000-list[x]*height,width,list[x]*height)
            pygame.draw.rect(self.screen, (255,255,255), bar)

    def make_colorbar(self,list,index):
        width = 1000/self.settings.num_val
        height = 1000/self.settings.max_val
        bar = pygame.Rect(index*width,1000-list[index]*height,width,list[index]*height)
        pygame.draw.rect(self.screen, (255,0,0), bar)

    def return_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    self.run_game()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        title=self.settings.font.render("Press 'TAB' to return to menu",True ,(255,255,255))
        text_quit=self.settings.font.render("Press 'Q' to Quit",True ,(255,255,255))
        self.screen.blit(title, (50, 50))
        self.screen.blit(text_quit, (50, 100))  
        pygame.display.update()
        

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.quicksort(self.nums,0,len(self.nums)-1)
                    while True:
                        self.return_menu()
                if event.key == pygame.K_2:
                    self.insertionsort(self.nums)
                    while True:
                        self.return_menu()
                if event.key == pygame.K_3:
                    self.selctionsort(self.nums)
                    while True:
                        self.return_menu()
                if event.key == pygame.K_4:
                    self.bubblesort(self.nums,len(self.nums)-1)
                    while True:
                        self.return_menu()
                #if event.key == pygame.K_5:
                #    self.mergesort(self.nums)
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

    def _update_screen(self):
        self.screen.fill((0,0,0))
        self.make_bars(self.nums)
        pygame.display.update()

    def menu(self):
        self.nums = []
        for x in range(self.settings.num_val):
            self.nums.append(random.randint(0,self.settings.max_val))
        self.screen.fill((0,0,0))
        title=self.settings.font.render("Sort Vivualiver",True ,(255,255,255))
        text1=self.settings.font.render("Press '1' for Quicksort",True ,(255,255,255))
        text2=self.settings.font.render("Press '2' for Insertionsort",True ,(255,255,255))
        text3=self.settings.font.render("Press '3' for Selectionsort",True ,(255,255,255))
        text4=self.settings.font.render("Press '4' for Bubblesort",True ,(255,255,255))
        text_quit=self.settings.font.render("Press 'Q' to Quit",True ,(255,255,255))
        text1_rect=text1.get_rect()
        text2_rect=text2.get_rect()
        text3_rect=text3.get_rect()
        text4_rect=text4.get_rect()
        title_rect=title.get_rect()
        quit_rect=text_quit.get_rect()
        # Main Menu Text
        self.screen.blit(title, (1000/2 - (title_rect[2]/2), 80))
        self.screen.blit(text1, (1000/2 - (text1_rect[2]/2), 360))
        self.screen.blit(text2, (1000/2 - (text2_rect[2]/2), 420))
        self.screen.blit(text3, (1000/2 - (text3_rect[2]/2), 480))
        self.screen.blit(text4, (1000/2 - (text4_rect[2]/2), 540))
        self.screen.blit(text_quit, (1000/2 - (quit_rect[2]/2), 600))
        pygame.display.update()

    def run_game(self):
        while True:
            self.menu()
            self._check_events()

if __name__=="__main__":
    v = Visualizer()
    v.run_game()

    
