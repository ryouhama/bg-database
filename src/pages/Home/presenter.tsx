import { Box, useColorModeValue } from '@chakra-ui/react'
import { SidebarContent, SideBarNavItem } from '../../components/SideBar'
// TODO: 設定だけFeatherIconなので、後でいいの探す
import { FiSettings } from 'react-icons/fi'
import { BiLineChart, BiPencil, BiHome, } from 'react-icons/bi'
import { IconType } from 'react-icons'

const LinkItems: {name: string, icon: IconType}[] = [
  { name: 'ホーム', icon: BiHome },
  { name: 'レート', icon: BiLineChart },
  { name: '記録', icon: BiPencil },
  { name: '設定', icon: FiSettings },
]

export const HomePresenter = () => {
  return (
    <Box minH="100vh" bg={useColorModeValue('gray.100', 'gray.900')}>
      {/* 固定サイドバーであるため、`onClose`は利用しない */}
      <SidebarContent onClose={() => undefined} display={{ base: 'none', md: 'block' }} >
        {LinkItems.map((link) =>(
          <SideBarNavItem key={link.name} icon={link.icon}>
            {link.name}
          </SideBarNavItem>
        ))}
      </SidebarContent>
      <Box ml={{ base: 0, md: 60 }} p="4">
        This is Content
      </Box>
    </Box>
  )
}
