import { Box, Flex, type FlexProps, Icon } from '@chakra-ui/react'
import { FC } from 'react'
import { IconType } from 'react-icons'

type Props = FlexProps & {
  icon: IconType
  children: string | number
}

export const SideBarNavItem: FC<Props> = (props) => {
  const { icon, children, ...rest } = props
  return (
    <Box
      as="a"
      href="#"
      style={{ textDecoration: 'none' }}
      _focus={{ boxShadow: 'none' }}>
      <Flex
        align="center"
        p="4"
        mx="4"
        borderRadius="lg"
        role="group"
        cursor="pointer"
        _hover={{
          bg: 'cyan.300',
          color: 'white',
        }}
        {...rest}>
        {icon && (
          <Icon
            mr="4"
            fontSize="16"
            _groupHover={{
              color: 'white',
            }}
            as={icon}
          />
        )}
        {children}
      </Flex>
    </Box>
  )
}
